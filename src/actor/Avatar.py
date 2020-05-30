from panda3d.core import CollideMask, CollisionNode, CollisionTube, GeomNode, NodePath, TextNode, Vec4
from direct.actor.Actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from src.gamebase import GameGlobals, BitmaskGlobals
from src.gamebase import TheGloriousGameLocalizer as GameLocalizer
from src.enemy.ShadowCaster import ShadowCaster
import random

SILLY_SURGE_CHANCE = 10

class Avatar(Actor, ShadowCaster):
    notify = DirectNotifyGlobal.directNotify.newCategory('Avatar')

    def __init__(self, other = None):
        Actor.__init__(self, None, None, other, flattenable=0, setFinal=1)
        ShadowCaster.__init__(self)
        self.collTube = None
        self.scale = 1.0
        self.height = 0.0
        self.style = None
        self.hpText = None
        self.hpTextGenerator = TextNode('HpTextGenerator')

    def delete(self):
        try:
            self.Avatar_deleted
        except:
            Actor.cleanup(self)
            self.Avatar_deleted = 1
            self.style = None
            self.collTube = None
            self.hpText = None
            self.hpTextGenerator = None
            ShadowCaster.delete(self)
            Actor.delete(self)

    def uniqueName(self, name):
        return 'Avatar-{0}-{1}'.format(id(self), name)

    def getCollisionId(self):
        return self.uniqueName('bodyColl')

    def getAvatarScale(self):
        return self.scale

    def setAvatarScale(self, scale):
        if self.scale != scale:
            self.scale = scale
            self.getGeomNode().setScale(scale)
            self.setHeight(self.height)

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height
        if not self.collTube:
            self.initializeBodyCollisions()
        self.collTube.setPointB(0, 0, height - self.getRadius())
        if self.collNodePath:
            self.collNodePath.forceRecomputeBounds()

    def getRadius(self):
        return GameGlobals.AvatarDefaultRadius

    def getStyle(self):
        return self.style

    def setStyle(self, style):
        self.style = style

    def getAirborneHeight(self):
        height = self.getPos(self.shadowPlacer.shadowNodePath)
        return height.getZ() + 0.025

    def initializeBodyCollisions(self):
        self.collTube = CollisionTube(0, 0, 0.5, 0, 0, self.height - self.getRadius(), self.getRadius())
        self.collNode = CollisionNode(self.getCollisionId())
        self.collNode.addSolid(self.collTube)
        self.collNodePath = self.attachNewNode(self.collNode)
        self.collNode.setCollideMask(BitmaskGlobals.WallBitmask)

    def showNodePathColl(self):
        self.collNodePath.show()


    def stashBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.stash()

    def unstashBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.unstash()

    def disableBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.removeNode()
            del self.collNodePath
        self.collTube = None

    def showHpText(self, number, bonus = 0, scale = 1.75):
        if number == 0:
            return

        if self.hpText:
             self.hideHpText()

        self.hpTextGenerator.setFont(GameGlobals.getSignFont())

        if number < 0:
            text = str(number)

            if random.randrange(0, 100) < SILLY_SURGE_CHANCE:
                text += '\n'
                text += random.choice(GameLocalizer.SillySurgeTerms)
        else:
            text = '+' + str(number)

        self.hpTextGenerator.setText(text)
        self.hpTextGenerator.clearShadow()
        self.hpTextGenerator.setAlign(TextNode.ACenter)
    
        if bonus == 1:          
            color = [1, 1, 0, 1]
        elif bonus == 2:
            color = [1, 0.5, 0, 1]
        elif number < 0:    
            color = [0.9, 0, 0, 1]
        else:
            color = [0, 0.9, 0, 1]

        self.hpTextGenerator.setTextColor(*color)
        self.hpTextNode = self.hpTextGenerator.generate()
        self.hpText = self.attachNewNode(self.hpTextNode)
        self.hpText.setScale(scale)
        self.hpText.setBillboardPointEye()
        self.hpText.setBin('fixed', 100)

        self.hpText.setPos(0, 0, self.height / 2)
            
        color[3] = 0
            
        Sequence(
            self.hpText.posInterval(1.0, (0, 0, self.height + 0.75), blendType='easeOut'),
            Wait(0.85),
            self.hpText.colorInterval(0.1, Vec4(*color), 0.1),
            Func(self.hideHpText)
        ).start()

    def hideHpText(self):
        if self.hpText:
            taskMgr.remove(self.uniqueName('hpText'))
            self.hpText.removeNode()
            self.hpText = None