import math, random

from direct.controls.GravityWalker import GravityWalker
from direct.directnotify import DirectNotifyGlobal
#from direct.distributed import #DistributedObject
from direct.gui.DirectButton import DirectButton, TextNode
from direct.gui.DirectGui import DGG
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectLabel import DirectLabel
from direct.interval.FunctionInterval import Func, Wait
from direct.interval.LerpInterval import LerpColorScaleInterval
from direct.interval.MetaInterval import Sequence
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBaseGlobal import globalClock
from direct.task.Task import Task, CollisionHandlerEvent
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import NodePath, CollisionSphere, CollisionNode, Point3, Vec3, VBase4, PandaNode, ClockObject, \
    CollisionTraverser, Texture, GraphicsOutput
from direct.directnotify.DirectNotifyGlobal import directNotify

from src.gamebase import Trajectory
from src.gamebase import GameGlobals
from src.gamebase import BitmaskGlobals

#cr = client repository > distributed / toontown client repository
# d_ = probably stands for distributed
from src.gamebase.BitmaskGlobals import WallBitmask
from src.actor import PieThrow

GROUND_PLANE_MIN = 0
CANNON_ROTATION_MIN = -55
CANNON_ROTATION_MAX = 50
CANNON_ROTATION_VEL = 15.0
CANNON_ANGLE_MIN = -45
CANNON_START_ANGLE = -10
# should be -15 at the end of the day
CANNON_ANGLE_MAX = 0
CANNON_ANGLE_VEL = 15.0
INITIAL_VELOCITY = 250
CANNON_MOVE_UPDATE_FREQ = 0.5
CAMERA_PULLBACK_MIN = 20
CAMERA_PULLBACK_MAX = 40
CANNON_Z = 20.25

GAG_START_BIAS = Vec3(0, 0, 0)

PIE_PITCH = 315

# pie appears when fireCannonTask is already done?

#We need to deprecate ClockDelta as much as we can!

#We don't need #DistributedObjects here because we don't work with networking yet
class DirectCannon(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DirectCannon')
    notify.setInfo(True)
    LOCAL_CANNON_MOVE_TASK = 'localCannonMoveTask'
    FIRE_KEY = 'control'
    UP_KEY = 'arrow_up'
    DOWN_KEY = 'arrow_down'
    LEFT_KEY = 'arrow_left'
    RIGHT_KEY = 'arrow_right'
    HIT_GROUND = 0

    def __init__(self, arena):
        self.arena = arena
        self.index = None
        self.gag = loader.loadModel("phase_3.5/models/props/tart.bam")
        self.nodePath = NodePath('Cannon')
        self.cannonsActive = 0
        self.cannonLocation = None
        self.cannonPostion = None
        self.cannon = None
        self.flashingLabel = None
        self.reloadingLabel = None
        self.madeGui = 0
        self.GagScale = None
        self.t = 0
        self.lastT = 0
        self.deltaT = 0
        self.hitTrack = None
        self.flyColNode = None
        self.flyColNodePath = None
        self.model_Created = 0
        self.cannonMoving = 0
        self.aimPad = None

    def disable(self):
        self.__unmakeGui()
        self.unloadDynamic()

    def delete(self):
        self.unload()

    def generateGravity(self, NodePath):
        base.cTrav = CollisionTraverser()
        GravityController = GravityWalker(legacyLifter=True)
        GravityController.setWallBitMask(BitmaskGlobals.WallBitmask)
        GravityController.setFloorBitMask(BitmaskGlobals.FloorBitmask)
        GravityController.initializeCollisions(base.cTrav, NodePath, floorOffset=0.025, reach=4.0)

    def setPosHpr(self, x, y, z, h, p, r):
        self.nodePath.setPosHpr(x, y, z, h, p, r)

    def getSphereRadius(self):
        return 1.5

    def getParentNodePath(self):
        return render

    def place(self):
        return self.cannon.place()

    def setIndex(self, index):
        self.index = index

    def load(self): #maybe add another param to choose what nodepath to be reparented to (like the toonhq)
        self.cannon = loader.loadModel('phase_4/models/minigames/toon_cannon.bam')
        self.cannon.find('**/square_drop_shadow').hide()
        self.sndCannonMove = base.loader.loadSfx('phase_4/audio/sfx/MG_cannon_adjust.ogg')
        self.sndCannonFire = base.loader.loadSfx('phase_4/audio/sfx/MG_cannon_fire_alt.ogg')
        self.sndHitGround = base.loader.loadSfx('phase_4/audio/sfx/MG_cannon_hit_dirt.ogg')

        self.cannon.reparentTo(self.nodePath)

        self.cannon.setZ(CANNON_Z)
        self.flashingLabel = None
        return self

    def unload(self):
        if self.cannon:
            # Fix camera
            if base.camera.getParent() in (self.barrel, self.cannon):
                base.camera.wrtReparentTo(render)

            self.cannon.removeNode()
            self.cannon = None

        self.unloadDynamic()

    def unloadDynamic(self):
        if self.hitTrack and self.hitTrack.isPlaying():
            self.hitTrack.finish()
        if self.flashingLabel and self.flashingLabel.isPlaying():
            self.flashingLabel.pause()
        
        self.__killLocalCannonMoveTask()
        taskMgr.remove('fireCannon')
        taskMgr.remove('flyTask')
        self.hitTrack = None
        self.flashingLabel = None
        self.__unmakeGui()

        if self.flyColNodePath:
            self.flyColNodePath.removeNode()
            self.flyColNodePath = None
        if self.reloadingLabel:
            self.reloadingLabel.destroy()
            self.reloadingLabel = None
        if self.gag:
            self.gag.removeNode()
            self.gag = None

        self.sndCannonMove = None
        self.sndCannonFire = None
        self.sndHitGround = None
        self.flyColNode = None

    def setReloading(self, reloading):
        if reloading:
            self.reloadingLabel.show()
        else:
            self.reloadingLabel.hide()

    def activateCannons(self):
        if not self.cannonsActive:
            self.cannonsActive = 1
            self.onstage()
            self.nodePath.reparentTo(self.getParentNodePath())

    def onstage(self):
        self.__createCannon()
        self.cannon.reparentTo(self.nodePath)

    def offstage(self):
        if self.cannon:
            self.cannon.reparentTo(hidden)

    def __createCannon(self):
        self.barrel = self.cannon.find('**/cannon')
        #self.barrel.setP(-20)
        self.cannonLocation = Point3(0, 0, CANNON_Z)
        self.cannonPosition = [0, CANNON_START_ANGLE]
        self.cannon.setPos(self.cannonLocation)
        self.__updateCannonPosition()

    def updateCannonPosition(self, zRot, angle):
        self.cannonPosition = [zRot, angle]
        self.__updateCannonPosition()

    def setMovie(self, mode, extraInfo):
        if mode == GameGlobals.CANNON_MOVIE_CLEAR:
            self.setLanded()
        elif mode == GameGlobals.CANNON_MOVIE_LANDED:
            self.setLanded()
        elif mode == GameGlobals.CANNON_MOVIE_FORCE_EXIT:
            self.setLanded()
        elif mode == GameGlobals.CANNON_MOVIE_LOAD:
            self.cannonBallsLeft = extraInfo
            self.__makeGui()
            camera.reparentTo(self.barrel)
            camera.setPos(0.5, -2, 2.5)
            camera.setHpr(0, 0, 0)
            self.__createPieModel()

    def __makeGui(self):
        if self.madeGui:
            return
        guiModel = 'phase_4/models/gui/cannon_game_gui.bam'
        cannonGui = loader.loadModel(guiModel)
        self.aimPad = DirectFrame(image=cannonGui.find('**/CannonFire_PAD'), relief=None, pos=(0.7, 0, -0.553333), scale=0.8)
        cannonGui.removeNode()
        self.fireButton = DirectButton(parent=self.aimPad, image=((guiModel, '**/Fire_Btn_UP'), (guiModel, '**/Fire_Btn_DN'), (guiModel, '**/Fire_Btn_RLVR')), relief=None, pos=(0.0115741, 0, 0.00505051), scale=1.0, command=self.__firePressed)
        self.upButton = DirectButton(parent=self.aimPad, image=((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief=None, pos=(0.0115741, 0, 0.221717))
        self.downButton = DirectButton(parent=self.aimPad, image=((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief=None, pos=(0.0136112, 0, -0.210101), image_hpr=(0, 0, 180))
        self.leftButton = DirectButton(parent=self.aimPad, image=((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief=None, pos=(-0.199352, 0, -0.000505269), image_hpr=(0, 0, -90))
        self.rightButton = DirectButton(parent=self.aimPad, image=((guiModel, '**/Cannon_Arrow_UP'), (guiModel, '**/Cannon_Arrow_DN'), (guiModel, '**/Cannon_Arrow_RLVR')), relief=None, pos=(0.219167, 0, -0.00101024), image_hpr=(0, 0, 90))
        guiClose = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui.bam')
        cannonBallText = '%d/%d' % (self.cannonBallsLeft, GameGlobals.CannonAmmo)
        self.cannonBallLabel = DirectLabel(parent=self.aimPad, text=cannonBallText, text_fg=VBase4(1, 1, 1, 1), text_align=TextNode.ACenter, relief=None, pos=(0.475, 0.0, -0.35), scale=0.25)
        self.cannonBallLabel.hide()
        self.reloadingLabel = DirectLabel(base.a2dBottomLeft, relief=None, text='Reloading...', text_scale=0.06, text_align=TextNode.ALeft, text_font=GameGlobals.getSignFont(), text_fg=(0.8, 0.8, 0.8, 1), text_shadow=(0, 0, 0, 1), pos=(0.2, 0, 0.2))
        self.reloadingLabel.hide()
        # temp commenting this out because python 2.7 gay
        #if self.cannonBallsLeft < 5:
        #    if self.flashingLabel:
        #        self.flashingLabel.stop()
        #    flashingTrack = Sequence()
        #    for i in range(10):
        #        flashingTrack.append(LerpColorScaleInterval(self.cannonBallLabel, 0.5, VBase4(1, 0, 0, 1)))
        #        flashingTrack.append(LerpColorScaleInterval(self.cannonBallLabel, 0.5, VBase4(1, 1, 1, 1)))
        #
        #    self.flashingLabel = flashingTrack
        #    self.flashingLabel.start()
        self.aimPad.setColor(1, 1, 1, 0.9)

        def bindButton(button, upHandler, downHandler):
            button.bind(DGG.B1PRESS, lambda x, handler = upHandler: handler())
            button.bind(DGG.B1RELEASE, lambda x, handler = downHandler: handler())

        bindButton(self.upButton, self.__upPressed, self.__upReleased)
        bindButton(self.downButton, self.__downPressed, self.__downReleased)
        bindButton(self.leftButton, self.__leftPressed, self.__leftReleased)
        bindButton(self.rightButton, self.__rightPressed, self.__rightReleased)
        self.__enableAimInterface()
        self.madeGui = 1

    def __unmakeGui(self):
        if not self.madeGui:
            return

        self.__disableAimInterface()
        self.upButton.unbind(DGG.B1PRESS)
        self.upButton.unbind(DGG.B1RELEASE)
        self.downButton.unbind(DGG.B1PRESS)
        self.downButton.unbind(DGG.B1RELEASE)
        self.leftButton.unbind(DGG.B1PRESS)
        self.leftButton.unbind(DGG.B1RELEASE)
        self.rightButton.unbind(DGG.B1PRESS)
        self.rightButton.unbind(DGG.B1RELEASE)

        if self.aimPad:
            self.aimPad.destroy()
            self.aimPad = None

        self.fireButton = None
        self.upButton = None
        self.downButton = None
        self.leftButton = None
        self.rightButton = None
        self.madeGui = 0
        self.notify.info('__unmakeGui >> successful')

    def __enableAimInterface(self):
        self.aimPad.show()
        self.accept(self.FIRE_KEY, self.__fireKeyPressed)
        self.accept(self.UP_KEY, self.__upKeyPressed)
        self.accept(self.DOWN_KEY, self.__downKeyPressed)
        self.accept(self.LEFT_KEY, self.__leftKeyPressed)
        self.accept(self.RIGHT_KEY, self.__rightKeyPressed)
        self.__spawnLocalCannonMoveTask()

    def __disableAimInterface(self):
        if self.aimPad:
            self.aimPad.hide()

        self.ignore(self.FIRE_KEY)
        self.ignore(self.UP_KEY)
        self.ignore(self.DOWN_KEY)
        self.ignore(self.LEFT_KEY)
        self.ignore(self.RIGHT_KEY)
        self.ignore(self.FIRE_KEY + '-up')
        self.ignore(self.UP_KEY + '-up')
        self.ignore(self.DOWN_KEY + '-up')
        self.ignore(self.LEFT_KEY + '-up')
        self.ignore(self.RIGHT_KEY + '-up')
        self.__killLocalCannonMoveTask()

    def __fireKeyPressed(self):
        self.ignore(self.FIRE_KEY)
        self.accept(self.FIRE_KEY + '-up', self.__fireKeyReleased)
        self.__firePressed()

    def __upKeyPressed(self):
        self.ignore(self.UP_KEY)
        self.accept(self.UP_KEY + '-up', self.__upKeyReleased)
        self.__upPressed()

    def __downKeyPressed(self):
        self.ignore(self.DOWN_KEY)
        self.accept(self.DOWN_KEY + '-up', self.__downKeyReleased)
        self.__downPressed()

    def __leftKeyPressed(self):
        self.ignore(self.LEFT_KEY)
        self.accept(self.LEFT_KEY + '-up', self.__leftKeyReleased)
        self.__leftPressed()

    def __rightKeyPressed(self):
        self.ignore(self.RIGHT_KEY)
        self.accept(self.RIGHT_KEY + '-up', self.__rightKeyReleased)
        self.__rightPressed()

    def __fireKeyReleased(self):
        self.ignore(self.FIRE_KEY + '-up')
        self.accept(self.FIRE_KEY, self.__fireKeyPressed)

    def __leftKeyReleased(self):
        self.ignore(self.LEFT_KEY + '-up')
        self.accept(self.LEFT_KEY, self.__leftKeyPressed)
        self.__leftReleased()

    def __rightKeyReleased(self):
        self.ignore(self.RIGHT_KEY + '-up')
        self.accept(self.RIGHT_KEY, self.__rightKeyPressed)
        self.__rightReleased()

    def __upKeyReleased(self):
        self.ignore(self.UP_KEY + '-up')
        self.accept(self.UP_KEY, self.__upKeyPressed)
        self.__upReleased()

    def __downKeyReleased(self):
        self.ignore(self.DOWN_KEY + '-up')
        self.accept(self.DOWN_KEY, self.__downKeyPressed)
        self.__downReleased()

    def __firePressed(self):
        self.notify.info('fire pressed')
        self.__unmakeGui()
        return self.setCannonLit(self.cannonPosition[0], self.cannonPosition[1])

    def setCannonLit(self, zRot, angle):
        #if self.boss.getCannonBallsLeft(avId) == 0:
        #    self.notify.info('ignoring setCannonList since no balls left for %s' % avId)
        #    return
        self.notify.info('setCannonLit: ' + ': zRot=' + str(zRot) + ', angle=' + str(angle))
        fireTime = GameGlobals.FUSE_TIME
        return self.setCannonWillFire(
         fireTime,
         zRot,
         angle)
        #self.boss.decrementCannonBallsLeft(avId)


    def __upPressed(self):
        self.notify.info('up pressed')
        self.upPressed = self.__enterControlActive(self.upPressed)

    def __downPressed(self):
        self.notify.info('down pressed')
        self.downPressed = self.__enterControlActive(self.downPressed)

    def __leftPressed(self):
        self.notify.info('left pressed')
        self.leftPressed = self.__enterControlActive(self.leftPressed)

    def __rightPressed(self):
        self.notify.info('right pressed')
        self.rightPressed = self.__enterControlActive(self.rightPressed)

    def __upReleased(self):
        self.notify.info('up released')
        self.upPressed = self.__exitControlActive(self.upPressed)

    def __downReleased(self):
        self.notify.info('down released')
        self.downPressed = self.__exitControlActive(self.downPressed)

    def __leftReleased(self):
        self.notify.info('left released')
        self.leftPressed = self.__exitControlActive(self.leftPressed)

    def __rightReleased(self):
        self.notify.info('right released')
        self.rightPressed = self.__exitControlActive(self.rightPressed)

    def __enterControlActive(self, control):
        return control + 1

    def __exitControlActive(self, control):
        return max(0, control - 1)

    def __spawnLocalCannonMoveTask(self):
        self.leftPressed = 0
        self.rightPressed = 0
        self.upPressed = 0
        self.downPressed = 0
        self.cannonMoving = 0
        task = Task(self.__localCannonMoveTask)
        task.lastPositionBroadcastTime = 0.0
        taskMgr.add(task, self.LOCAL_CANNON_MOVE_TASK)

    def __killLocalCannonMoveTask(self):
        taskMgr.remove(self.LOCAL_CANNON_MOVE_TASK)
        if self.cannonMoving and self.sndCannonMove:
            self.sndCannonMove.stop()

    def __localCannonMoveTask(self, task):
        pos = self.cannonPosition
        oldRot = pos[0]
        oldAng = pos[1]
        rotVel = 0
        if self.leftPressed:
            rotVel += CANNON_ROTATION_VEL
        if self.rightPressed:
            rotVel -= CANNON_ROTATION_VEL
        pos[0] += rotVel * globalClock.getDt()
        if pos[0] < CANNON_ROTATION_MIN:
            pos[0] = CANNON_ROTATION_MIN
        elif pos[0] > CANNON_ROTATION_MAX:
            pos[0] = CANNON_ROTATION_MAX
        angVel = 0
        if self.upPressed:
            angVel += CANNON_ANGLE_VEL
        if self.downPressed:
            angVel -= CANNON_ANGLE_VEL
        pos[1] += angVel * globalClock.getDt()
        if pos[1] < CANNON_ANGLE_MIN:
            pos[1] = CANNON_ANGLE_MIN
        elif pos[1] > CANNON_ANGLE_MAX:
            pos[1] = CANNON_ANGLE_MAX
        if oldRot != pos[0] or oldAng != pos[1]:
            if self.cannonMoving == 0:
                self.cannonMoving = 1
                base.playSfx(self.sndCannonMove, looping=1)
            self.__updateCannonPosition()
        elif self.cannonMoving:
            self.cannonMoving = 0
            if self.sndCannonMove:
                self.sndCannonMove.stop()
        return Task.cont

    def __updateCannonPosition(self):
        self.cannon.setHpr(self.cannonPosition[0], 0.0, 0.0)
        self.barrel.setHpr(0.0, self.cannonPosition[1], 0.0)

    def __createPieModel(self):
        self.model_Created = 1
        self.gag = loader.loadModel("phase_3.5/models/props/tart.bam")
        self.GagScale = self.gag.getScale()
        GagModelParent = render.attachNewNode('GagOriginChange')
        # this just changes what the gag looks like in the cannon
        self.gag.wrtReparentTo(GagModelParent)
        #self.gag.setPosHpr(0, 0, -1, 0, -90, 0)
        self.gag = GagModelParent
        self.__loadPieInCannon()

    def __destroyToonModels(self):
        if self.gag != None:
            self.gag.removeNode()
            self.gag = None
        self.model_Created = 0
        return

    def __loadPieInCannon(self):
        self.gag.reparentTo(self.barrel)
        self.gag.setPosHpr(0, 6, 0, 0, PIE_PITCH, 0)
        sc = self.GagScale
        self.gag.setScale(render, sc[0], sc[1], sc[2]) #uhh could this break something?

    def exitCannon(self):
        self.__unmakeGui()
        self.__resetPropToCannon()

    def __resetPropToCannon(self, FiredProp):
        pos = None
        if FiredProp:
            if hasattr(self, 'cannon') and self.cannon:
                FiredProp.reparentTo(self.cannon)
                FiredProp.setPosHpr(0, 6, 0, 0, PIE_PITCH, 0) #was causin me some weird problems
                FiredProp.wrtReparentTo(render)
            self.__resetFiredProp(FiredProp)
        return

    def __resetFiredProp(self, avatar, pos = None):
        if avatar:
            self.__stopCollisionHandler(avatar)
            self.setLanded()

    def __stopCollisionHandler(self, avatar):
        if avatar:
            self.flyColNode = None
            self.flyColSphere = None

            if self.flyColNodePath:
                #traverser.removeCollider(self.flyColNodePath)
                self.flyColNodePath.removeNode()
            
            self.flyColNodePath = None
            self.handler = None


    def setLanded(self):
        self.setMovie(GameGlobals.CANNON_MOVIE_LOAD, self.cannonBallsLeft - 1)

    def setCannonWillFire(self, fireTime, zRot, angle):
        self.notify.info('setCannonWillFire: ' + ': zRot=' + str(zRot) + ', angle=' + str(angle) + ', time=' + str(fireTime))
        #if not self.model_Created:
        #    self.notify.warning("We walked into the zone mid-flight, so we won't see it")
        #    return
        self.cannonPosition[0] = zRot
        self.cannonPosition[1] = angle
        self.__updateCannonPosition()
        task = Task(self.__fireCannonTask)
        task.fireTime = fireTime
        #if task.fireTime < 0.0:
        #    task.fireTime = 0.0
        taskMgr.add(task, 'fireCannon')
        self.notify.info('done with setCannonWillFire') #this DOES get printed btw

    def __fireCannonTask(self, task):
        launchTime = task.fireTime
        results = self.__calcFlightResults(launchTime)
        startPos, startHpr, startVel, trajectory, timeOfImpact, hitWhat = results

        if not results:
            return

        self.notify.info('start position: ' + str(startPos))
        self.notify.info('start velocity: ' + str(startVel))
        self.notify.info('time of launch: ' + str(launchTime))
        self.notify.info('time of impact: ' + str(timeOfImpact))
        self.notify.info('location of impact: ' + str(trajectory.getPos(timeOfImpact)))
        self.notify.info('start hpr: ' + str(startHpr))

        FlyingProp = self.gag

        self.generateGravity(FlyingProp)
        FlyingProp.reparentTo(render)
        FlyingProp.setPos(startPos)
        barrelHpr = self.barrel.getHpr(render)
        FlyingProp.setHpr(startHpr)
        #FlyingProp.setH(90)
        #self.gag.setPosHpr(0, 0, 100, 0, 0, 0) # this seems to be affecting the collision sphere btw
        info = {}
        info['trajectory'] = trajectory
        info['launchTime'] = launchTime
        info['timeOfImpact'] = timeOfImpact
        info['hitWhat'] = hitWhat
        info['flyingProp'] = self.gag
        info['hRot'] = self.cannonPosition[0]
        info['haveWhistled'] = 0
        info['maxCamPullback'] = CAMERA_PULLBACK_MIN
        self.flyColSphere = CollisionSphere(0, 0, 0, 1.2)
        self.flyColNode = CollisionNode('flySphere')
        self.flyColNode.setCollideMask(BitmaskGlobals.FloorBitmask | BitmaskGlobals.WallBitmask)
        self.flyColNode.addSolid(self.flyColSphere)
        self.flyColNodePath = self.gag.attachNewNode(self.flyColNode)
        self.flyColNodePath.setColor(1, 0, 0, 1)
        # self.flyColNodePath.show()
        self.handler = CollisionHandlerEvent()
        self.handler.setInPattern('cannonHit')
        # uh oh no work! :( << nevermind, should work now
        base.cTrav.addCollider(self.flyColNodePath, self.handler)
        print('Cannon pos: {0}'.format(self.cannon.getPos(render)))
        self.accept('cannonHit', self.__handleCannonHit)
        base.playSfx(self.sndCannonFire)
        flyTask = Task(self.__flyTask, 'flyTask')
        flyTask.info = info
        taskMgr.add(flyTask, 'flyTask')
        self.acceptOnce('stopFlyTask', self.__stopFlyTask)
        self.notify.info('done with __fireCannonTask')
        return Task.done

    def __toRadians(self, angle):
        return angle * 2.0 * math.pi / 360.0

    def __toDegrees(self, angle):
        return angle * 360.0 / (2.0 * math.pi)

    def __calcFlightResults(self, launchTime):
        if not self.gag:
            return

        self.generateGravity(self.gag)
        startPos = self.gag.getPos(render)
        startPos += GAG_START_BIAS
        startHpr = self.gag.getHpr(render)
        hpr = self.barrel.getHpr(render)
        rotation = self.__toRadians(hpr[0])
        angle = self.__toRadians(hpr[1])
        horizVel = INITIAL_VELOCITY * math.cos(angle)
        xVel = horizVel * -math.sin(rotation)
        yVel = horizVel * math.cos(rotation)
        zVel = INITIAL_VELOCITY * math.sin(angle)
        startVel = Vec3(xVel, yVel, zVel)
        trajectory = Trajectory.Trajectory(launchTime, startPos, startVel)
        self.trajectory = trajectory
        timeOfImpact, hitWhat = self.__calcGagImpact(trajectory)
        self.notify.info(
              'calcFlightResults(%s): '
              'rotation(%s), '
              'angle(%s), '
              'horizVel(%s), '
              'xVel(%s), '
              'yVel(%s), '
              'zVel(%s), '
              'startVel(%s), '
              'trajectory(%s), '
              'hitWhat(%s)' % (self.gag,
                 rotation,
                 angle,
                 horizVel,
                 xVel,
                 yVel,
                 zVel,
                 startVel,
                 trajectory,
                 hitWhat))

        # timeOfImpact, hitWhat = self.__calcToonImpact(trajectory, towerList)

        return startPos, startHpr, startVel, trajectory, 3 * timeOfImpact, hitWhat

    def __calcGagImpact(self, trajectory):
        t_groundImpact = trajectory.checkCollisionWithGround(GROUND_PLANE_MIN)
        if t_groundImpact >= trajectory.getStartTime():
            self.notify.info('gag impacts ground')
            return (t_groundImpact, self.HIT_GROUND)
        else:
            self.notify.error('__calcGagImpact: gag never impacts ground?')
            return (0.0, self.HIT_GROUND)

    def __handleCannonHit(self, collisionEntry):
        if not self.gag:
            return
        self.notify.info('__handleCannonHit')
        #if  == None or self.flyColNode == None:
        #    return
        interPt = collisionEntry.getSurfacePoint(render)
        hitNode = collisionEntry.getIntoNode().getName()
        fromNodePath = collisionEntry.getFromNodePath()
        intoNodePath = collisionEntry.getIntoNodePath()

        print('Pie hit: {0}'.format(hitNode))

        self.__stopFlyTask()
        self.__stopCollisionHandler(self.gag)

        track = Sequence()
        track.append(self.__hitSomething(hitNode))
        track.append(Func(self.setReloading, True))
        track.append(Wait(0.2))
        track.append(Func(self.setReloading, False))
        track.append(Func(self.setLanded))

        if self.hitTrack:
            self.hitTrack.finish()

        self.hitTrack = track
        self.hitTrack.start()

    def enterCannonHit(self, collisionEntry):
        pass

    def __flyTask(self, task):
        GagProp = task.info['flyingProp']
        if (not GagProp) or GagProp.isEmpty():
            return Task.done
        #if GagProp.isEmpty():
        #    self.__resetPropToCannon()
        #    return Task.done
        curTime = task.time + task.info['launchTime']
        t = min(curTime, task.info['timeOfImpact'])
        self.lastT = self.t
        self.t = t
        deltaT = self.t - self.lastT
        self.deltaT = deltaT
        if t >= task.info['timeOfImpact']:
            self.__resetPropToCannon(GagProp)
            return Task.done
        pos = task.info['trajectory'].getPos(t)
        GagProp.setFluidPos(pos)
        vel = task.info['trajectory'].getVel(t)
        run = math.sqrt(vel[0] * vel[0] + vel[1] * vel[1])
        rise = vel[2]
        theta = self.__toDegrees(math.atan(rise / run))
        GagProp.setP(PIE_PITCH + theta)
        return Task.cont

    def __stopFlyTask(self):
        self.notify.info('__stopFlyTask')
        taskMgr.remove('flyTask')

    def __hitSomething(self, hitNode):
        pos = self.gag.getPos(render)
        self.gag.removeNode()
        self.gag = None

        track = Sequence()
        enemy = self.arena.getEnemyByCollName(hitNode)

        if enemy:
            track.append(Func(enemy.takeDamage))

        track.append(PieThrow.getPieSplatInterval(pos, 'creampie'))
        return track