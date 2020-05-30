from panda3d.core import Point3, Texture, Vec4
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.task.Task import Task
from src.scenefx import EffectsManager
from src.gamebase import BitmaskGlobals
from .EnemyDict import EnemyAnimations, DefaultEnemyAnimations
from . import EnemyGlobals, EnemyDNA
from src.actor import Avatar
import string

aSize = 6.06
bSize = 5.29
cSize = 4.14

ModelDict = {
    'a': ('/models/char/suitA-', 4),
    'b': ('/models/char/suitB-', 4),
    'c': ('/models/char/suitC-', 3.5)
}
TutorialModelDict = {
    'a': ('/models/char/suitA-', 4),
    'b': ('/models/char/suitB-', 4),
    'c': ('/models/char/suitC-', 3.5)
}
HeadModelDict = {
    'a': ('/models/char/suitA-', 4),
    'b': ('/models/char/suitB-', 4),
    'c': ('/models/char/suitC-', 3.5)
}

AllEnemies = (
    ('walk', 'walk'), ('run', 'walk'), ('neutral', 'neutral')
)
AllEnemiesMinigame = (
    ('victory', 'victory'),
    ('flail', 'flailing'),
    ('tug-o-war', 'tug-o-war'),
    ('slip-backward', 'slip-backward'),
    ('slip-forward', 'slip-forward')
)
AllEnemiesTutorialBattle = (
    ('lose', 'lose'), ('pie-small-react', 'pie-small'), ('squirt-small-react', 'squirt-small')
)
AllEnemiesBattle = (
    ('drop-react', 'anvil-drop'),
    ('flatten', 'drop'),
    ('flush', 'flush'),
    ('sidestep-left', 'sidestep-left'),
    ('sidestep-right', 'sidestep-right'),
    ('squirt-large-react', 'squirt-large'),
    ('landing', 'landing'),
    ('reach', 'walknreach'),
    ('rake-react', 'rake'),
    ('hypnotized', 'hypnotize'),
    ('soak', 'soak'),
    ('lured', 'lured')
)
EnemiesCEOBattle = (
    ('sit', 'sit'),
    ('sit-eat-in', 'sit-eat-in'),
    ('sit-eat-loop', 'sit-eat-loop'),
    ('sit-eat-out', 'sit-eat-out'),
    ('sit-angry', 'sit-angry'),
    ('sit-hungry-left', 'leftsit-hungry'),
    ('sit-hungry-right', 'rightsit-hungry'),
    ('sit-lose', 'sit-lose'),
    ('tray-walk', 'tray-walk'),
    ('tray-neutral', 'tray-neutral'),
    ('sit-lose', 'sit-lose')
)

def attachEnemyHead(node, enemyName):
    enemyIndex = EnemyDNA.enemyHeadTypes.index(enemyName)
    enemyDNA = EnemyDNA.EnemyDNA()
    enemyDNA.newEnemy(enemyName)
    enemy = Enemy()
    enemy.setDNA(enemyDNA)
    headParts = enemy.getHeadParts()
    head = node.attachNewNode('head')
    for part in headParts:
        copyPart = part.copyTo(head)
        copyPart.setDepthTest(1)
        copyPart.setDepthWrite(1)

    enemy.delete()
    enemy = None
    p1 = Point3()
    p2 = Point3()
    head.calcTightBounds(p1, p2)
    d = p2 - p1
    biggest = max(d[0], d[2])
    column = enemyIndex % EnemyDNA.enemiesPerDept
    s = (0.2 + column / 100.0) / biggest
    pos = -0.14 + (EnemyDNA.enemiesPerDept - column - 1) / 135.0
    head.setPosHprScale(0, 0, pos, 180, 0, 0, s, s, s)
    return head

def createKapowExplosionTrack(parent, pos=(0, 0, 4.1), scale=0.4):
    explosion = loader.loadModel('phase_3.5/models/props/explosion.bam')
    explosion.setBillboardPointEye()
    explosion.setDepthWrite(False)

    return Sequence(
        Func(explosion.reparentTo, parent),
        Func(explosion.setPos, pos),
        Func(explosion.setScale, scale),
        Wait(0.6),
        Func(explosion.removeNode)
    )

class Enemy(Avatar.Avatar):
    healthColors = (
        Vec4(0, 1, 0, 1),
        Vec4(1, 1, 0, 1),
        Vec4(1, 0.5, 0, 1),
        Vec4(1, 0, 0, 1),
        Vec4(0.3, 0.3, 0.3, 1)
    )
    healthGlowColors = (
        Vec4(0.25, 1, 0.25, 0.5),
        Vec4(1, 1, 0.25, 0.5),
        Vec4(1, 0.5, 0.25, 0.5),
        Vec4(1, 0.25, 0.25, 0.5),
        Vec4(0.3, 0.3, 0.3, 0)
    )
    medallionColors = {
        'c': Vec4(0.863, 0.776, 0.769, 1.0),
        's': Vec4(0.843, 0.745, 0.745, 1.0),
        'l': Vec4(0.749, 0.776, 0.824, 1.0),
        'm': Vec4(0.749, 0.769, 0.749, 1.0)
    }

    def __init__(self):
        try:
            self.Enemy_initialized
            return
        except:
            self.Enemy_initialized = 1

        Avatar.Avatar.__init__(self)
        self.loseActor = None
        self.leftHand = None
        self.rightHand = None
        self.shadowJoint = None
        self.nametagJoint = None
        self.headParts = []
        self.healthBar = None
        self.healthCondition = 0
        self.isDisguised = 0
        self.isWaiter = 0
        self.isRental = 0
        self.currHP = 110
        self.maxHP = 110

    def delete(self):
        try:
            self.Enemy_deleted
        except:
            self.Enemy_deleted = 1
            self.killBlinkTasks()
            if self.leftHand:
                self.leftHand.removeNode()
                self.leftHand = None
            if self.rightHand:
                self.rightHand.removeNode()
                self.rightHand = None
            if self.shadowJoint:
                self.shadowJoint.removeNode()
                self.shadowJoint = None
            if self.nametagJoint:
                self.nametagJoint.removeNode()
                self.nametagJoint = None
            if self.loseActor:
                self.loseActor.delete()
                self.loseActor = None
            for part in self.headParts:
                part.removeNode()

            self.headParts = []
            self.removeHealthBar()
            Avatar.Avatar.delete(self)

    def setMaxHp(self, maxHp):
        self.maxHP = maxHp

    def setHp(self, hp):
        self.currHP = hp

    def setHeight(self, height):
        Avatar.Avatar.setHeight(self, height)

    def getToken(self):
        return self.uniqueName('token')

    def getRadius(self):
        return 2

    def setDNA(self, dna):
        if self.style:
            return

        self.style = dna
        self.generateEnemy()
        self.initializeDropShadow()

    def getStyleName(self):
        return self.style.name

    def generateEnemy(self):
        dna = self.style
        self.headParts = []
        self.headColor = None
        self.headTexture = None
        self.loseActor = None
        self.isSkeleton = 0

        if dna.name in EnemyGlobals.enemyProperties:
            properties = EnemyGlobals.enemyProperties[dna.name]
            self.scale = properties[EnemyGlobals.SCALE_INDEX]
            self.handColor = properties[EnemyGlobals.HAND_COLOR_INDEX]

            if dna.name == 'cc':
                self.headColor = EnemyGlobals.ColdCallerHead

            self.generateBody()

            if properties[EnemyGlobals.HEAD_TEXTURE_INDEX]:
                self.headTexture = properties[EnemyGlobals.HEAD_TEXTURE_INDEX]

            for head in properties[EnemyGlobals.HEADS_INDEX]:
                self.generateHead(head)

            self.setHeight(properties[EnemyGlobals.HEIGHT_INDEX])

        self.getGeomNode().setScale(self.scale)
        self.generateHealthBar()
        self.generateCorporateMedallion()
        self.setBlend(frameBlend=True)

    def generateBody(self):
        animDict = self.generateAnimDict()
        filePrefix, bodyPhase = ModelDict[self.style.body]
        filepath = 'phase_3.5' + filePrefix + 'mod'
        self.loadModel(filepath)
        self.loadAnims(animDict)
        self.setEnemyClothes()

    def generateAnimDict(self):
        animDict = {}
        filePrefix, bodyPhase = ModelDict[self.style.body]
        for anim in AllEnemies:
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]

        for anim in AllEnemiesMinigame:
            animDict[anim[0]] = 'phase_4' + filePrefix + anim[1]

        for anim in AllEnemiesTutorialBattle:
            filePrefix, bodyPhase = TutorialModelDict[self.style.body]
            animDict[anim[0]] = 'phase_' + str(bodyPhase) + filePrefix + anim[1]

        for anim in AllEnemiesBattle:
            animDict[anim[0]] = 'phase_5' + filePrefix + anim[1]

        if self.style.body == 'a':
            animDict['neutral'] = 'phase_4/models/char/suitA-neutral'
            for anim in EnemiesCEOBattle:
                animDict[anim[0]] = 'phase_12/models/char/suitA-' + anim[1]
        elif self.style.body == 'b':
            animDict['neutral'] = 'phase_4/models/char/suitB-neutral'
            for anim in EnemiesCEOBattle:
                animDict[anim[0]] = 'phase_12/models/char/suitB-' + anim[1]
        elif self.style.body == 'c':
            animDict['neutral'] = 'phase_3.5/models/char/suitC-neutral'
            for anim in EnemiesCEOBattle:
                animDict[anim[0]] = 'phase_12/models/char/suitC-' + anim[1]

        for anim in EnemyAnimations.get(self.style.name, ()) + DefaultEnemyAnimations:
            phase = 'phase_' + str(anim[2])
            animDict[anim[0]] = phase + filePrefix + anim[1]


        return animDict

    def initializeBodyCollisions(self):
        Avatar.Avatar.initializeBodyCollisions(self)
        self.collNode.setCollideMask(self.collNode.getIntoCollideMask() | BitmaskGlobals.WallBitmask)

    def setEnemyClothes(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        dept = self.style.dept
        phase = 3.5

        torsoTex = loader.loadTexture('phase_%s/maps/%s_blazer.jpg' % (phase, dept))
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_%s/maps/%s_leg.jpg' % (phase, dept))
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_%s/maps/%s_sleeve.jpg' % (phase, dept))
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)
        modelRoot.find('**/hands').setColorScale(self.handColor)
        self.leftHand = self.find('**/joint_Lhold')
        self.rightHand = self.find('**/joint_Rhold')
        self.shadowJoint = self.find('**/joint_shadow')
        self.nametagJoint = self.find('**/joint_nameTag')

    def makeWaiter(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        self.isWaiter = 1
        torsoTex = loader.loadTexture('phase_3.5/maps/waiter_m_blazer.jpg')
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_3.5/maps/waiter_m_leg.jpg')
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_3.5/maps/waiter_m_sleeve.jpg')
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)

    def makeRentalSuit(self, enemyType, modelRoot = None):
        if not modelRoot:
            modelRoot = self.getGeomNode()
        if enemyType == 's':
            torsoTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_blazer.jpg')
            legTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_leg.jpg')
            armTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_sleeve.jpg')
            handTex = loader.loadTexture('phase_3.5/maps/tt_t_ene_sellbotRental_hand.jpg')
        else:
            self.notify.warning('No rental suit for cog type %s' % enemyType)
            return
        self.isRental = 1
        modelRoot.find('**/torso').setTexture(torsoTex, 1)
        modelRoot.find('**/arms').setTexture(armTex, 1)
        modelRoot.find('**/legs').setTexture(legTex, 1)
        modelRoot.find('**/hands').setTexture(handTex, 1)

    def generateHead(self, headType):
        filePrefix, phase = ModelDict[self.style.body]
        if self.style.dept == 'p':
            filePrefix = '/models/char/pressbot-'
            phase = 4
        headModel = loader.loadModel('phase_' + str(phase) + filePrefix + 'heads')
        headReferences = headModel.findAllMatches('**/' + headType)
        for i in range(0, headReferences.getNumPaths()):
            headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'joint_head')
            if self.headTexture:
                headTex = loader.loadTexture('phase_' + str(phase) + '/maps/' + self.headTexture)
                headTex.setMinfilter(Texture.FTLinearMipmapLinear)
                headTex.setMagfilter(Texture.FTLinear)
                headPart.setTexture(headTex, 1)
            if self.headColor:
                headPart.setColor(self.headColor)
            headPart.flattenStrong()
            self.headParts.append(headPart)
        headModel.removeNode()

    def generateCorporateTie(self, modelPath = None):
        if not modelPath:
            modelPath = self
        dept = self.style.dept
        tie = modelPath.find('**/tie')
        if tie.isEmpty():
            self.notify.warning('skelecog has no tie model!!!')
            return
        if dept == 'c':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_boss.jpg')
        elif dept == 's':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_sales.jpg')
        elif dept == 'l':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_legal.jpg')
        elif dept == 'm':
            tieTex = loader.loadTexture('phase_5/maps/cog_robot_tie_money.jpg')
        tieTex.setMinfilter(Texture.FTLinearMipmapLinear)
        tieTex.setMagfilter(Texture.FTLinear)
        tie.setTexture(tieTex, 1)

    def generateCorporateMedallion(self):
        icons = loader.loadModel('phase_3/models/gui/cog_icons')
        dept = self.style.dept
        chestNull = self.find('**/joint_attachMeter')
        if dept in EnemyDNA.enemyDeptModelPaths:
            self.corpMedallion = icons.find(EnemyDNA.enemyDeptModelPaths[dept]).copyTo(chestNull)
        self.corpMedallion.setPosHprScale(0.02, 0.05, 0.04, 180.0, 0.0, 0.0, 0.51, 0.51, 0.51)
        self.corpMedallion.setColor(self.medallionColors[dept])
        icons.removeNode()

    def generateHealthBar(self):
        self.removeHealthBar()
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        button.setScale(3.0)
        button.setH(180.0)
        button.setColor(self.healthColors[0])
        chestNull = self.find('**/def_joint_attachMeter')
        if chestNull.isEmpty():
            chestNull = self.find('**/joint_attachMeter')
        button.reparentTo(chestNull)
        self.healthBar = button
        glow = loader.loadModel('phase_3.5/models/props/glow')
        glow.reparentTo(self.healthBar)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(self.healthGlowColors[0])
        button.flattenLight()
        self.healthBarGlow = glow
        self.healthBar.hide()
        self.healthCondition = 0

    def reseatHealthBarForSkele(self):
        self.healthBar.setPos(0.0, 0.1, 0.0)

    def killBlinkTasks(self):
        try:
            taskMgr.remove(self.uniqueName('blink-task'))
        except AttributeError:
            self.notify.debug('Could not kill blink task.')

    def showHealthBar(self):
        if self.corpMedallion and not self.corpMedallion.isEmpty():
            self.corpMedallion.hide()
        if self.healthBar and not self.healthBar.isEmpty():
            self.healthBar.show()

    def hideHealthBar(self):
        if self.corpMedallion and not self.corpMedallion.isEmpty():
            self.corpMedallion.show()
        if self.healthBar and not self.healthBar.isEmpty():
            self.healthBar.hide()

    def updateHealthBar(self, forceUpdate=0):
        health = float(self.currHP) / float(self.maxHP)
        if health > 0.95:
            condition = 0
        elif health > 0.7:
            condition = 1
        elif health > 0.3:
            condition = 2
        elif health > 0.05:
            condition = 3
        elif health > 0.0:
            condition = 4
        else:
            condition = 5
        if self.healthCondition != condition or forceUpdate:
            self.killBlinkTasks()
            if condition == 4:
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            elif condition == 5:
                if self.healthCondition == 4:
                    taskMgr.remove(self.uniqueName('blink-task'))
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.uniqueName('blink-task'))
            else:
                self.healthBar.setColor(self.healthColors[condition], 1)
                self.healthBarGlow.setColor(self.healthGlowColors[condition], 1)
        self.healthCondition = condition

    def __blinkRed(self, task):
        if not self.healthBar:
            return Task.done
        self.healthBar.setColor(self.healthColors[3], 1)
        self.healthBarGlow.setColor(self.healthGlowColors[3], 1)
        if self.healthCondition == 5:
            self.healthBar.setScale(1.17)
        return Task.done

    def __blinkGray(self, task):
        if not self.healthBar:
            return Task.done
        self.healthBar.setColor(self.healthColors[4], 1)
        self.healthBarGlow.setColor(self.healthGlowColors[4], 1)
        if self.healthCondition == 5:
            self.healthBar.setScale(1.0)
        return Task.done

    def removeHealthBar(self):
        if self.healthBar:
            self.healthBar.removeNode()
            self.healthBar = None
        if self.healthCondition == 4 or self.healthCondition == 5:
            taskMgr.remove(self.uniqueName('blink-task'))
        self.healthCondition = 0
        return

    def getLoseActor(self):
        if self.loseActor == None:
            if not self.isSkeleton:
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseModel = 'phase_' + str(phase) + filePrefix + 'lose-mod'
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {'lose': loseAnim})
                loseNeck = self.loseActor.find('**/joint_head')
                for part in self.headParts:
                    part.instanceTo(loseNeck)

                if self.isWaiter:
                    self.makeWaiter(self.loseActor)
                else:
                    self.setEnemyClothes(self.loseActor)
            else:
                loseModel = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-lose-mod'
                filePrefix, phase = TutorialModelDict[self.style.body]
                loseAnim = 'phase_' + str(phase) + filePrefix + 'lose'
                self.loseActor = Actor.Actor(loseModel, {'lose': loseAnim})
                self.generateCorporateTie(self.loseActor)
        self.loseActor.setScale(self.scale)
        self.loseActor.setPos(self.getPos(render))
        self.loseActor.setHpr(self.getHpr(render))
        self.loseActor.setBlend(frameBlend=True)
        shadowJoint = self.loseActor.find('**/joint_shadow')
        dropShadow = loader.loadModel('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.45)
        dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
        dropShadow.reparentTo(shadowJoint)
        return self.loseActor

    def cleanupLoseActor(self):
        self.notify.debug('cleanupLoseActor()')
        if self.loseActor != None:
            self.notify.debug('cleanupLoseActor() - got one')
            self.loseActor.cleanup()
        self.loseActor = None
        return

    def makeSkeleton(self):
        model = 'phase_5/models/char/cog' + string.upper(self.style.body) + '_robot-zero'
        anims = self.generateAnimDict()
        anim = self.getCurrentAnim()
        dropShadow = self.dropShadow
        if not dropShadow.isEmpty():
            dropShadow.reparentTo(hidden)
        self.removePart('modelRoot')
        self.loadModel(model)
        self.loadAnims(anims)
        self.getGeomNode().setScale(self.scale * 1.0173)
        self.generateHealthBar()
        self.generateCorporateMedallion()
        self.generateCorporateTie()
        self.setHeight(self.height)
        parts = self.findAllMatches('**/pPlane*')
        for partNum in range(0, parts.getNumPaths()):
            bb = parts.getPath(partNum)
            bb.setTwoSided(1)

        self.leftHand = self.find('**/joint_Lhold')
        self.rightHand = self.find('**/joint_Rhold')
        self.shadowJoint = self.find('**/joint_shadow')
        self.nametagNull = self.find('**/joint_nameTag')
        if not dropShadow.isEmpty():
            dropShadow.setScale(0.75)
            if not self.shadowJoint.isEmpty():
                dropShadow.reparentTo(self.shadowJoint)
        self.loop(anim)
        self.isSkeleton = 1
        self.setBlend(frameBlend=True)


    def getExplosionTrack(self):
        loseActor = self.getLoseActor()
        spinningSound = loader.loadSfx('phase_3.5/audio/sfx/Cog_Death.ogg')
        deathSound = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')
        explosionInterval = Sequence(
            Func(loseActor.reparentTo, render),
            Func(self.stash),
            ActorInterval(loseActor, 'lose', duration=6.1),
            Func(loseActor.hide)
        )
        deathSoundTrack = Sequence(
            Wait(0.6),
            SoundInterval(spinningSound, duration=1.2, startTime=1.5, volume=0.2),
            SoundInterval(spinningSound, duration=3.0, startTime=0.6, volume=0.8),
            SoundInterval(deathSound, volume=0.32)
        )
        smallGears = EffectsManager.createParticleEffect(file='gearExplosionSmall')
        singleGear = EffectsManager.createParticleEffect('GearExplosion', numParticles=1)
        smallGearExplosion = EffectsManager.createParticleEffect('GearExplosion', numParticles=10)
        bigGearExplosion = EffectsManager.createParticleEffect('BigGearExplosion', numParticles=30)
        gearPoint = Point3(loseActor.getX(), loseActor.getY(), loseActor.getZ())
        smallGears.setDepthWrite(False)
        singleGear.setDepthWrite(False)
        smallGearExplosion.setDepthWrite(False)
        bigGearExplosion.setDepthWrite(False)

        explosionTrack = Sequence()
        explosionTrack.append(Wait(5.4))
        explosionTrack.append(createKapowExplosionTrack(loseActor))
        gears1Track = Sequence(
            Wait(2.0),
            ParticleInterval(smallGears, loseActor, worldRelative=0, duration=4.3, cleanup=True)
        )
        gears2MTrack = Track(
            (0.0, explosionTrack),
            (0.7, ParticleInterval(singleGear, loseActor, worldRelative=0, duration=5.7, cleanup=True)),
            (5.2, ParticleInterval(smallGearExplosion, loseActor, worldRelative=0, duration=1.2, cleanup=True)),
            (5.4, ParticleInterval(bigGearExplosion, loseActor, worldRelative=0, duration=1.0, cleanup=True))
        )
        return Sequence(
            Parallel(explosionInterval, deathSoundTrack, gears1Track, gears2MTrack),
            Func(self.cleanupLoseActor),
            Func(self.delete)
        )

    def getHeadParts(self):
        return self.headParts

    def getRightHand(self):
        return self.rightHand

    def getLeftHand(self):
        return self.leftHand

    def getShadowJoint(self):
        return self.shadowJoint