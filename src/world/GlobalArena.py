"""
GlobalArena.py
Description:
    - The classfile that contains all of the 3D elements of the main scene.
"""
from direct.controls.GravityWalker import GravityWalker
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.gui.OnscreenImage import OnscreenImage, TransparencyAttrib
from direct.showbase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showutil import Effects
from panda3d.core import NodePath, PandaNode, WindowProperties, CollisionTraverser, TextNode, Vec3

from src.actor import LandwalkerAvatarControls
from src.battle.HQLaffMeter import HQLaffMeter
from src.battle.GameOverScreen import GameOverScreen
from src.battle import DirectCannon
from src.gamebase import GameGlobals, BitmaskGlobals, GameLoader
from src.world.Landwalker import actor
from src.enemy import EnemyLoader, Enemy
from src.enemyai.GameEnemy import GameEnemy
from src.enemy.EnemyDNA import EnemyDNA
from src.enemyai.EnemyGrid import EnemyGrid
import random

RoundEnemyCounts = [5, 10, 13, 17]

class GlobalArena(DirectObject):

    def __init__(self, base):
        DirectObject.__init__(self)
        self.base = base
        self.crosshair = None
        self.hqLaffMeter = None
        self.roundLabel = None
        self.intermissionLabel = None
        self.tempHQ = None
        self.background = None
        self.sky = None
        self.round = 0
        self.enemiesLeft = 0
        self.enemies = []

        pass
        # we should probably move this stuff somewhere else
        # if we continue with this idea, we must get rid of the gui since it'll become redundant
        #curProps = base.win.getProperties()
        #props = WindowProperties()
        #props.setOrigin(curProps.getXOrigin() + 1, curProps.getYOrigin() + 1)
        #props.setCursorHidden(True)
        #base.win.requestProperties(props)

    def unload(self):
        taskMgr.remove('arenaSpawnEnemy')
        taskMgr.remove('endIntermission')

        for enemy in list(self.enemies):
            enemy.delete()

        self.enemies = []

        if self.cannon:
            self.cannon.delete()
            self.cannon = None

        self.unloadBackground()
        self.unloadGUI()
        self.enemyGrid = None
        self.ignoreAll()

    def unloadBackground(self):
        if self.tempHQ:
            self.tempHQ.removeNode()
            self.tempHQ = None

        if self.background:
            self.background.removeNode()
            self.background = None

        if self.sky:
            self.sky.removeNode()
            self.sky = None

        self.tunnelOrigin = None

    def unloadGUI(self):
        if self.crosshair:
            self.crosshair.destroy()
            self.crosshair = None
        if self.hqLaffMeter:
            self.hqLaffMeter.destroy()
            self.hqLaffMeter = None
        if self.roundLabel:
            self.roundLabel.destroy()
            self.roundLabel = None
        if self.intermissionLabel:
            self.intermissionLabel.destroy()
            self.intermissionLabel = None
        if self.cannon:
            self.cannon.unloadDynamic()

    def freezeGame(self):
        for enemy in list(self.enemies):
            enemy.fsm.request('Off')

        taskMgr.remove('arenaSpawnEnemy')

    def getAliveEnemies(self):
        return [enemy for enemy in self.enemies if enemy.isAlive()]

    def getEnemyByCollName(self, collName):
        for enemy in self.enemies:
            if enemy.getCollisionId() == collName:
                return enemy

    def getHQHitPoint(self):
        return self.tempHQ.getPos(render)

    def loadCrosshair(self):
        if self.crosshair:
            return
    
        self.crosshair = OnscreenImage(image = 'custom/xhair.png', pos = (0,0,0), scale = 0.05)
        self.crosshair.setTransparency(TransparencyAttrib.MAlpha)

    def showCrosshair(self):
        if self.crosshair:
            self.crosshair.show()

    def hideCrosshair(self):
        if self.crosshair:
            self.crosshair.hide()

    def load(self):
        # this should be renovated later once we get BattleArea worked on.
        self.loadBackground()
        self.loadCannon()
        self.loadGUI()
        self.loadEnemies()
        self.loadSky()
        self.loadCrosshair()
        self.loadMusic()

    def damageHQ(self):
        damageTaken = random.randrange(GameGlobals.AttackMinHP, GameGlobals.AttackMaxHP)

        if self.hqLaffMeter:
            self.hqLaffMeter.takeDamage(damageTaken)

    def loadBackground(self):
        self.background = loader.loadModel("tutorial_street.bam")
        self.background.reparentTo(render)
        self.background.setH(270)
        self.background.find('**/tunnel_sphere').removeNode()
        hq = self.background.find('**/*toon_landmark_hqTT_DNARoot')
        self.tempHQ = loader.loadModel('phase_3.5/models/modules/hqTEST2-mod.egg')
        self.tempHQ.reparentTo(hq)
        self.tempHQ.wrtReparentTo(render)
        self.tempHQ.find('**/rimCollisions').removeNode()
        hq.hide()

        self.tunnelOrigin = self.background.find('**/tunnel_origin')

    def loadGUI(self):
        self.hqLaffMeter = HQLaffMeter()
        self.roundLabel = DirectLabel(base.a2dBottomLeft, relief=None, text='Round 1 / 1', text_scale=0.08, text_align=TextNode.ALeft, text_font=GameGlobals.getSignFont(), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), pos=(0.2, 0, 0.1))
        self.intermissionLabel = DirectLabel(base.a2dTopCenter, relief=None, text='Intermission', text_scale=0.12, text_align=TextNode.ACenter, text_font=GameGlobals.getSignFont(), text_fg=(0, 1, 0, 1), text_shadow=(0, 0.7, 0, 1), pos=(0, 0, -0.5))
        self.intermissionLabel.hide()
    
    def loadMusic(self):
        base.playMusic(loader.loadMusic('phase_4/audio/bgm/MG_CogThief_ttoff.ogg'), volume=0.4, looping=True)

    def loadSky(self):
        self.sky = loader.loadModel('phase_9/models/cogHQ/cog_sky.bam')
        skyInner = self.sky.find('**/InnerGroup')
        skyMiddle = self.sky.find('**/MiddleGroup')
        skyOuter = self.sky.find('**/OutterSky')

        if not skyOuter.isEmpty():
            skyOuter.setBin('background', 0)
        if not skyMiddle.isEmpty():
            skyMiddle.setDepthWrite(0)
            skyMiddle.setBin('background', 10)
        if not skyInner.isEmpty():
            skyInner.setDepthWrite(0)
            skyInner.setBin('background', 20)

        # Hood.py @ ln 214
        self.sky.reparentTo(base.camera)
        self.sky.wrtReparentTo(render)
        self.sky.setZ(0.0)
        self.sky.setHpr(0.0, 0.0, 0.0)

    def loadCannon(self):
        self.cannon = DirectCannon.DirectCannon(self)
        self.cannon.load()
        self.cannon.activateCannons()
        self.cannon.setMovie(GameGlobals.CANNON_MOVIE_LOAD, 10)

        self.cannon.cannon.reparentTo(self.tempHQ.find('**/group1/hat/rim'))

    def loadEnemies(self):
        EnemyLoader.loadModels()
        EnemyLoader.loadEnemyModelsAndAnims()
        EnemyLoader.loadDialog()
        EnemyLoader.loadSkelDialog()

        self.enemyGrid = EnemyGrid(startX=0, startY=-55, z=0, xIncrement=7.5, yIncrement=-7.5, xSize=6, ySize=4)
        self.enemies = []

        self.startFirstRound()
        self.spawnEnemy()
        taskMgr.doMethodLater(self.getNextRespawnTime(), self.spawnEnemy, 'arenaSpawnEnemy')
        self.accept('enemyDied', self.__enemyDied)
        self.accept('hqDefeated', self.__hqDefeated)

    def getNextRespawnTime(self):
        return random.uniform(3.5, 5.0)

    def spawnEnemy(self, task=None):
        if not self.enemyGrid:
            return

        if task:
            task.delayTime = self.getNextRespawnTime()

        if len(self.enemies) >= self.enemyGrid.getMaxEnemies():
            return Task.again

        # Can't spawn enemies during intermission
        if not self.intermissionLabel.isHidden():
            return Task.again

        # We don't have any enemies left in this round
        if self.enemiesLeft <= 0:
            return Task.again

        enemy = GameEnemy(self)
        self.enemies.append(enemy)
        dna = EnemyDNA()
        dna.newEnemyRandom()
        enemy.setDNA(dna)
        enemy.showHealthBar()
        enemy.fsm.request('TunnelIn', [self.tunnelOrigin])

        self.enemiesLeft -= 1
        return Task.again
    
    def __enemyDied(self, enemy):
        if self.enemiesLeft <= 0 and len(self.enemies) == 1 and not self.getAliveEnemies():
            self.setRound(self.round + 1, intermission=True)

    def __hqDefeated(self):
        self.loseGame()

    def startFirstRound(self):
        self.setRound(0, intermission=False)
    
    def setRound(self, round, intermission=False):
        # We won the game!!!
        if round >= len(RoundEnemyCounts):
            self.winGame()
            return

        self.round = round
        self.enemiesLeft = RoundEnemyCounts[self.round]
        self.roundLabel['text'] = 'Round {0} of {1}'.format(self.round + 1, len(RoundEnemyCounts))

        if intermission:
            # Start intermission
            self.hqLaffMeter.heal(GameGlobals.IntermissionHealHP)

            self.intermissionLabel.show()
            loader.loadSfx('phase_3.5/audio/sfx/tt_s_gui_sbk_cdrSuccess.ogg').play()

            taskMgr.doMethodLater(10.0, self.endIntermission, 'endIntermission')

    def endIntermission(self, task=None):
        self.intermissionLabel.hide()

    def resetCannon(self):
        self.cannon.cannon.setZ(18)
        self.cannon.barrel.setHpr(0, 20, 0)

    def winGame(self):
        self.unloadGUI()
        self.freezeGame()

        winMusic = loader.loadMusic('phase_4/audio/sfx/outro_win.ogg')
        boatSfx = loader.loadSfx('phase_5/audio/sfx/AA_drop_boat.ogg')

        ship = loader.loadModel('phase_5/models/props/ship')
        ship.find('**/shadow').removeNode()
        ship.setPos(20, -8, 30)
        ship.setHpr(90, 0, 0)
        ship.setScale(1.25)
        endingPos = Vec3(20, -8, 0)

        self.winSequence = Sequence(
            Func(camera.wrtReparentTo, render),
            Func(base.playMusic, winMusic),
            camera.posHprInterval(3.0, (20.4823, -60.423, 3), (0, 10, 0), blendType='easeInOut'),
            Wait(2),
            Func(boatSfx.play),
            Func(ship.reparentTo, render),
            ship.posInterval(2, endingPos),
            Effects.createZBounce(ship, 2, endingPos, 0.5, 1.5),
            Wait(3.5),
            Func(ship.removeNode),
            Func(self.gameOver, win=True)
        )
        self.winSequence.start()

    def loseGame(self):
        self.unloadGUI()
        self.freezeGame()

        enemySequence = Parallel()

        for enemy in list(self.enemies):
            if enemy.isAlive():
                enemySequence.append(Sequence(
                    Func(enemy.getLeftHand().getChildren().hide),
                    Func(enemy.getRightHand().getChildren().hide),
                    enemy.actorInterval('victory')
                ))
            else:
                enemy.delete()

        loseSound = loader.loadMusic('phase_4/audio/sfx/outro_sad.ogg')
        explosionSfx = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')

        cannonExplosionPos = self.cannon.cannon.getPos(render) + Vec3(0, 0, 5.1)
        cannonFinalPos = self.cannon.cannon.getPos()
        cannonFinalPos.setZ(16)

        self.loseSequence = Sequence(
            Func(camera.wrtReparentTo, render),
            Func(self.resetCannon),
            Func(base.playMusic, loseSound),
            camera.posHprInterval(2.0, (20.4823, -18.423, 6), (180, 10, 0), blendType='easeInOut'),
            Parallel(
                enemySequence,
                Sequence(
                    Wait(2.5),
                    Func(self.cannon.cannon.setTransparency, True),
                    Func(explosionSfx.play),
                    Parallel(
                        Enemy.createKapowExplosionTrack(render, pos=cannonExplosionPos, scale=1.5),
                        self.cannon.cannon.posInterval(1, cannonFinalPos, blendType='easeInOut'),
                        self.cannon.barrel.hprInterval(1, (0, 110, 0), blendType='easeInOut'),
                        self.cannon.cannon.colorScaleInterval(1, (1, 1, 1, 0), blendType='easeInOut'),
                    ),
                    
                )
            ),
            Func(self.gameOver, win=False)
        )
        self.loseSequence.start()
    
    def gameOver(self, win):
        self.unload()
        screen = GameOverScreen(win)
        screen.load()
        screen.enter()