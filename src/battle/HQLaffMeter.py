from panda3d.core import *
from direct.gui.DirectGui import *
from src.gamebase import GameGlobals
from src.enemy import EnemyHealthBar

class HQLaffMeter(DirectFrame):
    
    def __init__(self):
        DirectFrame.__init__(self, relief=None, image='phase_14/maps/toonhq_meter.png', image_scale=Vec3(1, 1, 0.27) * 0.6)
        self.initialiseoptions(HQLaffMeter)
        self.setTransparency(True)
        self.posInTopLeft()

        self.hpBar = DirectWaitBar(self, scale=0.5, pos=(0.15, 0, -0.01), frameSize=(-0.88, 0.88, -0.225, 0.225))
        self.hpBar.setBin('background', 10)
        self.pendingDamages = 0
        self.hpTask = self.uniqueName('hpTask')
        self.setMaxHp(GameGlobals.HQLaffPoints)

    def destroy(self):
        DirectFrame.destroy(self)

        if self.hpBar:
            self.hpBar.destroy()
            self.hpBar = None
        
        self.pendingDamages = 0
        taskMgr.remove(self.hpTask)

    def uniqueName(self, name):
        return 'HQLaffMeter-{0}-{1}'.format(id(self), name)

    def posInTopLeft(self):
        self.reparentTo(base.a2dTopLeft)
        self.setPos(0.8, 0, -0.2)
    
    def setMaxHp(self, maxHp):
        self.maxHp = maxHp
        self.hp = maxHp
        self.hpBar['range'] = maxHp
        self.hpBar['value'] = maxHp
        self.updateColor(self.hpBar)

    def heal(self, hp):
        self.takeDamage(-hp)

    def takeDamage(self, hp):
        self.pendingDamages += hp

        if not taskMgr.hasTaskNamed(self.hpTask):
            taskMgr.doMethodLater(0.025, self.__decrementHp, self.hpTask)
    
    def updateColor(self, bar):
        r, g, b, _ = EnemyHealthBar.HEALTH_COLORS[EnemyHealthBar.getHealthCondition(self.getPercentage(bar['value'], bar['range']))]
        bar['barColor'] = (r, g, b, 1)
        bar['frameColor'] = (r * 0.7, g * 0.7, b * 0.7, 1)

    def getPercentage(self, value, range):
        return float(value) / float(range)

    def __decrementHp(self, task):
        if self.pendingDamages > 0:
            self.hp -= 1
            self.pendingDamages -= 1
        else:
            if self.hp >= self.maxHp:
                self.pendingDamages = 0
                return task.done

            self.hp += 1
            self.pendingDamages += 1

        self.hpBar['value'] = self.hp
        self.updateColor(self.hpBar)

        if self.pendingDamages == 0:
            return task.done

        if self.hp <= 0:
            self.pendingDamages = 0
            messenger.send('hqDefeated')
            return task.done

        return task.again