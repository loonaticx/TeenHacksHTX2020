from panda3d.core import *
from panda3d.ai import *
from direct.showbase import PythonUtil
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.interval.IntervalGlobal import *
from src.enemy.Enemy import Enemy
from src.gamebase import GameGlobals, GameUtils
from src.enemyai import EnemyAttacks
import random

tunnelPivotPos = Vec3(-25, 6, 0)
pivotAngle = 90 + 45
pivotDur = 3.75

class GameEnemy(Enemy):

    def __init__(self, arena):
        Enemy.__init__(self)
        self.arena = arena
        self.aiCharacter = None
        self.spotToken = self.uniqueName('spot')
        self.lastAnimation = None
        self.tunnelSequence = None
        self.hurtSequence = None
        self.gridPos = None

        self.fsm = ClassicFSM('GameEnemy', [
            State('Off', self.enterOff, self.exitOff),
            State('TunnelIn', self.enterTunnelIn, self.exitTunnelIn),
            State('WalkToGrid', self.enterWalkToGrid, self.exitWalkToGrid),
            State('AttackHQ', self.enterAttackHQ, self.exitAttackHQ),
            State('Idle', self.enterIdle, self.exitIdle)
        ], 'Off', 'Off')
        self.fsm.enterInitialState()
    
    def announceDead(self):
        messenger.send('enemyDied', [self])

    def isAlive(self):
        return self.fsm.getCurrentState() != 'Off' and self.currHP > 0

    def delete(self):
        self.removeFromGame()

        if self.fsm.getCurrentState().getName() != 'Off':
            self.fsm.request('Off')

        if self in self.arena.enemies:
            self.arena.enemies.remove(self)

        Enemy.delete(self)
    
    def getGridPos(self):
        if self.gridPos is None:
            self.gridPos = self.arena.enemyGrid.occupyRandomSpot(self.spotToken)

        return self.gridPos

    def enableAI(self):
        if self.aiCharacter:
            print('Tried to enable AI when already enabled.')
            return

        self.aiCharacter = AICharacter(self.uniqueName('enemy'), self, 10, 12, 16)
        self.arena.aiWorld.addAiChar(self.aiCharacter)
    
    def disableAI(self):
        if not self.aiCharacter:
            print('Tried to disable AI when already disabled.')
            return

        self.arena.aiWorld.removeAiChar(self.uniqueName('enemy'))
        self.aiCharacter = None

    def pauseTunnel(self):
        if self.tunnelSequence:
            self.tunnelSequence.pause()

        self.tunnelSequence = None

    def setTunnelRunning(self, running):
        if not self.tunnelSequence:
            return

        if running:
            self.tunnelSequence.resume()
        else:
            self.tunnelSequence.pause()

    def loop(self, animName, restart = 1, partName = None, fromFrame = None, toFrame = None):
        # Keep track of the last played animation.
        result = Enemy.loop(self, animName, restart, partName, fromFrame, toFrame)
        self.lastAnimation = animName
        return result

    def takeDamage(self):
        if self.currHP <= 0:
            return

        if not self.lastAnimation:
            self.lastAnimation = self.getCurrentAnim()

        hpTaken = random.randrange(30, 50)
        self.currHP = max(0, self.currHP - hpTaken)
        self.showHpText(-hpTaken)
        self.updateHealthBar()

        if self.hurtSequence:
            self.hurtSequence.pause()

        if self.currHP > 0:
            self.hurtSequence = Sequence(
                Func(self.setTunnelRunning, False),
                Func(self.getLeftHand().getChildren().hide),
                Func(self.getRightHand().getChildren().hide),
                ActorInterval(self, 'pie-small-react'),
                Func(self.getLeftHand().getChildren().show),
                Func(self.getRightHand().getChildren().show),
                Func(self.loop, self.lastAnimation),
                Func(self.setTunnelRunning, True)
            )
        else:
            self.hurtSequence = Sequence(
                Func(self.pauseTunnel),
                self.getExplosionTrack(),
                Func(self.announceDead)
            )
        
        self.hurtSequence.start()

    def removeFromGame(self):
        if self.arena.enemyGrid:
            self.arena.enemyGrid.releaseSpot(self.spotToken)

        if self.hurtSequence:
            self.hurtSequence.pause()
            self.hurtSequence = None

        self.pauseTunnel()

    def enterOff(self):
        self.removeFromGame()

        if self.getCurrentAnim() != 'neutral':
            self.loop('neutral')

        if self.aiCharacter:
            self.disableAI()

    def exitOff(self):
        pass

    def enterTunnelIn(self, tunnel):
        self.pauseTunnel()
        pivotNode = tunnel.attachNewNode(self.uniqueName('pivotNode'))
        pivotNode.setPos(tunnelPivotPos)
        pivotNode.setHpr(0, 0, 0)
        endX = tunnel.getX(render) * 0.4
        pivotLerpDur = pivotDur * (90.0 / pivotAngle)
        self.reparentTo(pivotNode)
        self.setPos(0, 0, 0)
        self.setX(tunnel, endX)
        startX = self.getX()
        targetX = startX - random.uniform(1.0, 15.0)
        self.setHpr(tunnel, 0, 0, 0)
        pivotNode.setH(-pivotAngle)
        
        finalX = startX - random.uniform(10.5, 14.5)
        finalY = -48
        finalPos = Point3(finalX, finalY, 0)

        self.tunnelSequence = Sequence(
            Func(self.loop, 'walk'),
            Parallel(
                pivotNode.hprInterval(pivotDur, hpr=Point3(0, 0, 0), name=self.uniqueName('tunnelInPivot')),
                Sequence(
                    Wait(pivotDur - pivotLerpDur),
                    self.posInterval(pivotLerpDur, pos=Point3(targetX, 0, 0), name=self.uniqueName('tunnelInPivotLerpPos')),
                )
            ),
            Func(self.wrtReparentTo, render),
            Func(pivotNode.removeNode),
            Func(self.headsUp, finalPos),
            self.posInterval(pivotLerpDur + 1.0, pos=finalPos),
            Func(self.fsm.request, 'WalkToGrid')
        )
        self.tunnelSequence.start()

    def exitTunnelIn(self):
        self.pauseTunnel()

    def enterWalkToGrid(self):
        pos = self.getGridPos()
        targetHpr = GameUtils.getHeadsUpHpr(self.getPos(render), pos)
        targetHpr[0] = PythonUtil.fitDestAngle2Src(self.getH(), targetHpr[0])
        hqHpr = GameUtils.getHeadsUpHpr(pos, self.arena.tempHQ.getPos(render))
        hqHpr[0] = PythonUtil.fitDestAngle2Src(targetHpr[0], hqHpr[0])

        distance = (self.getPos() - pos).length()
        hDiff = abs(self.getH() - targetHpr.getX())
        hqHDiff = abs(targetHpr.getX() - hqHpr.getX())

        self.tunnelSequence = Sequence(
            Func(self.loop, 'walk'),
            self.hprInterval(hDiff / GameGlobals.EnemyTurnSpeed, targetHpr, blendType='easeInOut'),
            self.posInterval(distance / GameGlobals.EnemyForwardSpeed, pos, blendType='easeInOut'),
            self.hprInterval(hqHDiff / GameGlobals.EnemyTurnSpeed, hqHpr, blendType='easeInOut'),
            Func(self.loop, 'neutral'),
            Func(self.__reachedGrid)
        )
        self.tunnelSequence.start()
    
    def exitWalkToGrid(self):
        pass

    def __reachedGrid(self):
        if random.random() > 0.5:
            self.fsm.request('AttackHQ')
        else:
            self.fsm.request('Idle')

    def enterIdle(self, *args):
        pos = self.getGridPos()
        hpr = GameUtils.getHeadsUpHpr(pos, self.arena.tempHQ.getPos(render))
        self.reparentTo(render)
        self.setPosHpr(pos, hpr)

        if self.getCurrentAnim() != 'neutral':
            self.loop('neutral')

        taskMgr.doMethodLater(random.randrange(1.0, 10.0), self.attackNow, self.uniqueName('nextAttack'))

    def exitIdle(self):
        taskMgr.remove(self.uniqueName('nextAttack'))
    
    def enterAttackHQ(self):
        attack = EnemyAttacks.chooseAttack(self)
        hitPoint = self.arena.getHQHitPoint()
        self.pauseTunnel()

        self.tunnelSequence = Sequence(
            attack(self, hitPoint),
            Func(self.fsm.request, 'Idle')
        )
        self.tunnelSequence.start()

    def exitAttackHQ(self):
        self.pauseTunnel()
    
    def attackNow(self, task):
        if self.hurtSequence and self.hurtSequence.isPlaying():
            return task.again
        
        self.fsm.request('AttackHQ')