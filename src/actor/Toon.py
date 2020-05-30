from direct.directnotify import DirectNotifyGlobal
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.interval.IntervalGlobal import *
from direct.task.Task import Task
from panda3d.core import *
import random
import types
import math

from src.actor.ActorDict import *
from src.actor.ToonHead import ToonHead
from src.actor import ActorDict, ToonDNA, Avatar
from src.gamebase import BitmaskGlobals

DogDialogueArray = []
CatDialogueArray = []
HorseDialogueArray = []
RabbitDialogueArray = []
MouseDialogueArray = []
DuckDialogueArray = []
MonkeyDialogueArray = []
BearDialogueArray = []
PigDialogueArray = []
LegsAnimDict = {}
TorsoAnimDict = {}
HeadAnimDict = {}
Preloaded = {}


def loadModels():
    global Preloaded
    if not Preloaded:
        print('Preloading avatars...')

        for key in LegDict.keys():
            fileRoot = LegDict[key]
            Preloaded[fileRoot + '-1000'] = loader.loadModel('phase_3' + fileRoot + '1000.bam')
            print(Preloaded[fileRoot + '-1000'])


        for key in TorsoDict.keys():
            fileRoot = TorsoDict[key]

            Preloaded[fileRoot + '-1000'] = loader.loadModel('phase_3' + fileRoot + '1000.bam')

def loadBasicAnims():
    loadPhaseAnims()

def unloadBasicAnims():
    loadPhaseAnims(0)

def loadTutorialBattleAnims():
    loadPhaseAnims('phase_3.5')

def unloadTutorialBattleAnims():
    loadPhaseAnims('phase_3.5', 0)

def loadMinigameAnims():
    loadPhaseAnims('phase_4')

def unloadMinigameAnims():
    loadPhaseAnims('phase_4', 0)

def loadBattleAnims():
    loadPhaseAnims('phase_5')

def unloadBattleAnims():
    loadPhaseAnims('phase_5', 0)

def loadSellbotHQAnims():
    loadPhaseAnims('phase_9')

def unloadSellbotHQAnims():
    loadPhaseAnims('phase_9', 0)

def loadCashbotHQAnims():
    loadPhaseAnims('phase_10')

def unloadCashbotHQAnims():
    loadPhaseAnims('phase_10', 0)

def loadBossbotHQAnims():
    loadPhaseAnims('phase_12')

def unloadBossbotHQAnims():
    loadPhaseAnims('phase_12', 0)

def loadPhaseAnims(phaseStr = 'phase_3', loadFlag = 1):
    if phaseStr == 'phase_3':
        animList = Phase3AnimList
    elif phaseStr == 'phase_3.5':
        animList = Phase3_5AnimList
    elif phaseStr == 'phase_4':
        animList = Phase4AnimList
    elif phaseStr == 'phase_5':
        animList = Phase5AnimList
    elif phaseStr == 'phase_5.5':
        animList = Phase5_5AnimList
    elif phaseStr == 'phase_6':
        animList = Phase6AnimList
    elif phaseStr == 'phase_9':
        animList = Phase9AnimList
    elif phaseStr == 'phase_10':
        animList = Phase10AnimList
    elif phaseStr == 'phase_12':
        animList = Phase12AnimList
    else:
        self.notify.error('Unknown phase string %s' % phaseStr)
    for key in LegDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            elif anim[0] in LegsAnimDict[key]:
                if base.localAvatar.style.legs == key:
                    base.localAvatar.unloadAnims([anim[0]], 'legs', None)

    for key in TorsoDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            elif anim[0] in TorsoAnimDict[key]:
                if base.localAvatar.style.torso == key:
                    base.localAvatar.unloadAnims([anim[0]], 'torso', None)

    for key in HeadDict.keys():
        if key.find('d') >= 0:
            for anim in animList:
                if loadFlag:
                    pass
                elif anim[0] in HeadAnimDict[key]:
                    if base.localAvatar.style.head == key:
                        base.localAvatar.unloadAnims([anim[0]], 'head', None)

def compileGlobalAnimList():
    phaseList = [Phase3AnimList,
     Phase3_5AnimList,
     Phase4AnimList,
     Phase5AnimList,
     Phase5_5AnimList,
     Phase6AnimList,
     Phase9AnimList,
     Phase10AnimList,
     Phase12AnimList]
    phaseStrList = ['phase_3',
     'phase_3.5',
     'phase_4',
     'phase_5',
     'phase_5.5',
     'phase_6',
     'phase_9',
     'phase_10',
     'phase_12']
    for animList in phaseList:
        phaseStr = phaseStrList[phaseList.index(animList)]
        for key in LegDict.keys():
            LegsAnimDict.setdefault(key, {})
            for anim in animList:
                file = phaseStr + LegDict[key] + anim[1]
                LegsAnimDict[key][anim[0]] = file

        for key in TorsoDict.keys():
            TorsoAnimDict.setdefault(key, {})
            for anim in animList:
                file = phaseStr + TorsoDict[key] + anim[1]
                TorsoAnimDict[key][anim[0]] = file

        for key in HeadDict.keys():
            if key.find('d') >= 0:
                HeadAnimDict.setdefault(key, {})
                for anim in animList:
                    file = phaseStr + HeadDict[key] + anim[1]
                    HeadAnimDict[key][anim[0]] = file

def loadDialog():
    loadPath = 'phase_3.5/audio/dial/'

    DogDialogueFiles = ('AV_dog_short', 'AV_dog_med', 'AV_dog_long', 'AV_dog_question', 'AV_dog_exclaim', 'AV_dog_howl')
    global DogDialogueArray
    for file in DogDialogueFiles:
        DogDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    catDialogueFiles = ('AV_cat_short', 'AV_cat_med', 'AV_cat_long', 'AV_cat_question', 'AV_cat_exclaim', 'AV_cat_howl')
    global CatDialogueArray
    for file in catDialogueFiles:
        CatDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    horseDialogueFiles = ('AV_horse_short', 'AV_horse_med', 'AV_horse_long', 'AV_horse_question', 'AV_horse_exclaim', 'AV_horse_howl')
    global HorseDialogueArray
    for file in horseDialogueFiles:
        HorseDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    rabbitDialogueFiles = ('AV_rabbit_short', 'AV_rabbit_med', 'AV_rabbit_long', 'AV_rabbit_question', 'AV_rabbit_exclaim', 'AV_rabbit_howl')
    global RabbitDialogueArray
    for file in rabbitDialogueFiles:
        RabbitDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    mouseDialogueFiles = ('AV_mouse_short', 'AV_mouse_med', 'AV_mouse_long', 'AV_mouse_question', 'AV_mouse_exclaim', 'AV_mouse_howl')
    global MouseDialogueArray
    for file in mouseDialogueFiles:
        MouseDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    duckDialogueFiles = ('AV_duck_short', 'AV_duck_med', 'AV_duck_long', 'AV_duck_question', 'AV_duck_exclaim', 'AV_duck_howl')
    global DuckDialogueArray
    for file in duckDialogueFiles:
        DuckDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    monkeyDialogueFiles = ('AV_monkey_short', 'AV_monkey_med', 'AV_monkey_long', 'AV_monkey_question', 'AV_monkey_exclaim', 'AV_monkey_howl')
    global MonkeyDialogueArray
    for file in monkeyDialogueFiles:
        MonkeyDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    bearDialogueFiles = ('AV_bear_short', 'AV_bear_med', 'AV_bear_long', 'AV_bear_question', 'AV_bear_exclaim', 'AV_bear_howl')
    global BearDialogueArray
    for file in bearDialogueFiles:
        BearDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

    pigDialogueFiles = ('AV_pig_short', 'AV_pig_med', 'AV_pig_long', 'AV_pig_question', 'AV_pig_exclaim', 'AV_pig_howl')
    global PigDialogueArray
    for file in pigDialogueFiles:
        PigDialogueArray.append(base.loadSfx(loadPath + file + '.ogg'))

def unloadDialog():
    global CatDialogueArray
    global PigDialogueArray
    global BearDialogueArray
    global DuckDialogueArray
    global RabbitDialogueArray
    global MouseDialogueArray
    global DogDialogueArray
    global HorseDialogueArray
    global MonkeyDialogueArray
    DogDialogueArray = []
    CatDialogueArray = []
    HorseDialogueArray = []
    RabbitDialogueArray = []
    MouseDialogueArray = []
    DuckDialogueArray = []
    MonkeyDialogueArray = []
    BearDialogueArray = []
    PigDialogueArray = []

class Toon(Avatar.Avatar, ToonHead):
    notify = DirectNotifyGlobal.directNotify.newCategory('Toon')

    def __init__(self):
        Avatar.Avatar.__init__(self)
        ToonHead.__init__(self)
        try:
            self.Toon_initialized
            return
        except:
            self.Toon_initialized = 1

        self.avatarType = 'toon'
        self.soundChatBubble = base.loadSfx('phase_3/audio/sfx/GUI_balloon_popup.ogg')
        self.swimRunSfx = base.loadSfx('phase_4/audio/sfx/AV_footstep_runloop_water.ogg')
        self.swimRunLooping = False
        self.animFSM = ClassicFSM('Toon', [State('off', self.enterOff, self.exitOff),
         State('neutral', self.enterNeutral, self.exitNeutral)], 'off', 'off')

        animStateList = self.animFSM.getStates()
        self.animFSM.enterInitialState()



    def stopAnimations(self):
        if hasattr(self, 'animFSM'):
            if not self.animFSM.isInternalStateInFlux():
                self.animFSM.request('off')
            else:
                self.notify.warning('animFSM in flux, state=%s, not requesting off' % self.animFSM.getCurrentState().getName())
        else:
            self.notify.warning('animFSM has been deleted')
        if self.effectTrack != None:
            self.effectTrack.finish()
            self.effectTrack = None
        if self.emoteTrack != None:
            self.emoteTrack.finish()
            self.emoteTrack = None
        if self.stunTrack != None:
            self.stunTrack.finish()
            self.stunTrack = None
        if self.wake:
            self.wake.stop()
            self.wake.destroy()
            self.wake = None
        self.cleanupPieModel()
        return

    def delete(self):
        try:
            self.Toon_deleted
        except:
            self.Toon_deleted = 1
            self.stopAnimations()
            self.rightHands = None
            self.rightHand = None
            self.leftHands = None
            self.leftHand = None
            self.headParts = None
            self.torsoParts = None
            self.hipsParts = None
            self.legsParts = None
            del self.animFSM
            for bookActor in self.__bookActors:
                bookActor.cleanup()

            del self.__bookActors
            for holeActor in self.__holeActors:
                holeActor.cleanup()

            del self.__holeActors
            self.soundTeleport = None
            self.motion.delete()
            self.motion = None

            self.removeHeadMeter()
            self.removeGMIcon()
            self.removePartyHat()
            Avatar.Avatar.delete(self)
            ToonHead.delete(self)

    def updateToonDNA(self, newDNA, fForce = 0):
        self.newDNA = newDNA
        self.style.gender = newDNA.getGender()
        oldDNA = self.style
        if fForce or newDNA.head != oldDNA.head:
            self.swapToonHead(newDNA.head)
        if fForce or newDNA.torso != oldDNA.torso:
            self.swapToonTorso(newDNA.torso, genClothes=0)
            self.loop('neutral')
        if fForce or newDNA.legs != oldDNA.legs:
            self.swapToonLegs(newDNA.legs)
        self.swapToonColor(newDNA)
        self.__swapToonClothes(newDNA)

    def parentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                if base.config.GetBool('want-new-anims', 1):
                    if not self.getPart('torso', lodName).find('**/def_head').isEmpty():
                        self.attach('head', 'torso', 'def_head', lodName)
                    else:
                        self.attach('head', 'torso', 'joint_head', lodName)
                else:
                    self.attach('head', 'torso', 'joint_head', lodName)
                self.attach('torso', 'legs', 'joint_hips', lodName)

        else:
            self.attach('head', 'torso', 'joint_head')
            self.attach('torso', 'legs', 'joint_hips')

    def unparentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.getPart('head', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('torso', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('legs', lodName).reparentTo(self.getLOD(lodName))

        else:
            self.getPart('head').reparentTo(self.getGeomNode())
            self.getPart('torso').reparentTo(self.getGeomNode())
            self.getPart('legs').reparentTo(self.getGeomNode())

    def generateToon(self):
        self.setDNAString()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        #self.rescaleToon()
        #self.resetHeight()
        self.setupToonNodes()

    def setupToonNodes(self):
        rightHand = NodePath('rightHand')
        self.rightHand = None
        self.rightHands = []
        leftHand = NodePath('leftHand')
        self.leftHands = []
        self.leftHand = None
        for lodName in self.getLODNames():
            hand = self.getPart('torso', lodName).find('**/joint_Rhold')
            if base.config.GetBool('want-new-anims', 1):
                if not self.getPart('torso', lodName).find('**/def_joint_right_hold').isEmpty():
                    hand = self.getPart('torso', lodName).find('**/def_joint_right_hold')
            else:
                hand = self.getPart('torso', lodName).find('**/joint_Rhold')
            self.rightHands.append(hand)
            rightHand = rightHand.instanceTo(hand)
            if base.config.GetBool('want-new-anims', 1):
                if not self.getPart('torso', lodName).find('**/def_joint_left_hold').isEmpty():
                    hand = self.getPart('torso', lodName).find('**/def_joint_left_hold')
            else:
                hand = self.getPart('torso', lodName).find('**/joint_Lhold')
            self.leftHands.append(hand)
            leftHand = leftHand.instanceTo(hand)
            if self.rightHand == None:
                self.rightHand = rightHand
            if self.leftHand == None:
                self.leftHand = leftHand

        self.headParts = self.findAllMatches('**/__Actor_head')
        self.legsParts = self.findAllMatches('**/__Actor_legs')
        self.hipsParts = self.legsParts.findAllMatches('**/joint_hips')
        self.torsoParts = self.hipsParts.findAllMatches('**/__Actor_torso')
        return

    def initializeBodyCollisions(self, collIdStr):
        Avatar.Avatar.initializeBodyCollisions(self, collIdStr)
        if not self.ghostMode:
            self.collNode.setCollideMask(self.collNode.getIntoCollideMask() | BitmaskGlobals.PieBitmask)

    def generateToonLegs(self, copy = 1):
        global Preloaded
        legStyle = self.newDNA.legs
        filePrefix = LegDict.get(legStyle)
        if filePrefix is None:
            self.notify.error('unknown leg style: %s' % legStyle)
        print(Preloaded[filePrefix+'-1000'])
        # self.loadModel(Preloaded[filePrefix+'-1000'], 'legs', '1000', True)
        self.loadModel(Preloaded[filePrefix+'-1000'])
        if not copy:
            self.showPart('legs', '1000')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '1000')
        self.findAllMatches('**/boots_short').stash()
        self.findAllMatches('**/boots_long').stash()
        self.findAllMatches('**/shoes').stash()
        return

    def swapToonLegs(self, legStyle, copy = 1):
        self.unparentToonParts()
        self.removePart('legs', '1000')
        # Bugfix: Until upstream Panda3D includes this, we have to do it here.
        if 'legs' in self._Actor__commonBundleHandles:
            del self._Actor__commonBundleHandles['legs']
        self.style.legs = legStyle
        self.generateToonLegs(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        del self.shadowJoint
        self.initializeDropShadow()
        self.initializeNametag3d()

    def generateToonTorso(self, copy = 1, genClothes = 1):
        global Preloaded
        torsoStyle = self.style.torso
        filePrefix = TorsoDict.get(torsoStyle)
        if filePrefix is None:
            self.notify.error('unknown torso style: %s' % torsoStyle)
        self.loadModel(Preloaded[filePrefix+'-1000'], 'torso', '1000', True)
        if not copy:
            self.showPart('torso', '1000')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '1000')
        if genClothes == 1 and not len(torsoStyle) == 1:
            self.generateToonClothes()
        return

    def swapToonTorso(self, torsoStyle, copy = 1, genClothes = 1):
        self.unparentToonParts()
        self.removePart('torso', '1000')
        # Bugfix: Until upstream Panda3D includes this, we have to do it here.
        if 'torso' in self._Actor__commonBundleHandles:
            del self._Actor__commonBundleHandles['torso']
        self.style.torso = torsoStyle
        self.generateToonTorso(copy, genClothes)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.setupToonNodes()

    def setDNAString(self):
        self.newDNA = ToonDNA.ToonDNA()
        self.setDNA(self.newDNA)

    def setDNA(self, dna):
        self.style = dna
        #self.generateToon()

    def generateToonHead(self, copy = 1):
        headHeight = ToonHead.generateToonHead(self, copy, self.style, '1000')
        if self.style.getAnimal() == 'dog':
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '1000')

    def swapToonHead(self, headStyle=-1, copy = 1):
        self.stopLookAroundNow()
        self.eyelids.request('open')
        self.unparentToonParts()
        self.removePart('head', '1000')
        # Bugfix: Until upstream Panda3D includes this, we have to do it here.
        if 'head' in self._Actor__commonBundleHandles:
            del self._Actor__commonBundleHandles['head']
        if headStyle > -1:
            self.style.head = headStyle
        self.generateToonHead(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.eyelids.request('open')
        self.startLookAround()

    def generateToonColor(self):
        ToonHead.generateToonColor(self, self.style)
        armColor = self.style.getArmColor()
        gloveColor = self.style.getGloveColor()
        legColor = self.style.getLegColor()
        for lodName in self.getLODNames():
            torso = self.getPart('torso', lodName)
            if len(self.style.torso) == 1:
                parts = torso.findAllMatches('**/torso*')
                parts.setColor(*armColor)
            for pieceName in ('arms', 'neck'):
                piece = torso.find('**/' + pieceName)
                piece.setColor(*armColor)

            hands = torso.find('**/hands')
            hands.setColor(*gloveColor)
            legs = self.getPart('legs', lodName)
            for pieceName in ('legs', 'feet'):
                piece = legs.find('**/%s;+s' % pieceName)
                piece.setColor(*legColor)

        if self.cheesyEffect == ToontownGlobals.CEGreenToon:
            self.reapplyCheesyEffect()

    def swapToonColor(self, dna):
        self.setStyle(dna)
        self.generateToonColor()

    def __swapToonClothes(self, dna):
        self.setStyle(dna)
        self.generateToonClothes(fromNet=1)


    def generateToonClothes(self, fromNet = 0):
        swappedTorso = 0
        if self.hasLOD():
            if self.style.getGender() == 'f' and fromNet == 0:
                try:
                    bottomPair = ToonDNA.GirlBottoms[self.style.botTex]
                except:
                    bottomPair = ToonDNA.GirlBottoms[0]

                if len(self.style.torso) < 2:
                    self.sendLogSuspiciousEvent('nakedToonDNA %s was requested' % self.style.torso)
                    return 0
                elif self.style.torso[1] == 's' and bottomPair[1] == ToonDNA.SKIRT:
                    self.swapToonTorso(self.style.torso[0] + 'd', genClothes=0)
                    swappedTorso = 1
                elif self.style.torso[1] == 'd' and bottomPair[1] == ToonDNA.SHORTS:
                    self.swapToonTorso(self.style.torso[0] + 's', genClothes=0)
                    swappedTorso = 1
            try:
                texName = ToonDNA.Shirts[self.style.topTex]
            except:
                texName = ToonDNA.Shirts[0]

            shirtTex = loader.loadTexture(texName, okMissing=True)
            if shirtTex is None:
                self.sendLogSuspiciousEvent('failed to load texture %s' % texName)
                shirtTex = loader.loadTexture(ToonDNA.Shirts[0])
            shirtTex.setMinfilter(Texture.FTLinearMipmapLinear)
            shirtTex.setMagfilter(Texture.FTLinear)
            try:
                shirtColor = ToonDNA.ClothesColors[self.style.topTexColor]
            except:
                shirtColor = ToonDNA.ClothesColors[0]

            try:
                texName = ToonDNA.Sleeves[self.style.sleeveTex]
            except:
                texName = ToonDNA.Sleeves[0]

            sleeveTex = loader.loadTexture(texName, okMissing=True)
            if sleeveTex is None:
                self.sendLogSuspiciousEvent('failed to load texture %s' % texName)
                sleeveTex = loader.loadTexture(ToonDNA.Sleeves[0])
            sleeveTex.setMinfilter(Texture.FTLinearMipmapLinear)
            sleeveTex.setMagfilter(Texture.FTLinear)
            try:
                sleeveColor = ToonDNA.ClothesColors[self.style.sleeveTexColor]
            except:
                sleeveColor = ToonDNA.ClothesColors[0]

            if self.style.getGender() == 'm':
                try:
                    texName = ToonDNA.BoyShorts[self.style.botTex]
                except:
                    texName = ToonDNA.BoyShorts[0]

            else:
                try:
                    texName = ToonDNA.GirlBottoms[self.style.botTex][0]
                except:
                    texName = ToonDNA.GirlBottoms[0][0]

            bottomTex = loader.loadTexture(texName, okMissing=True)
            if bottomTex is None:
                self.sendLogSuspiciousEvent('failed to load texture %s' % texName)
                if self.style.getGender() == 'm':
                    bottomTex = loader.loadTexture(ToonDNA.BoyShorts[0])
                else:
                    bottomTex = loader.loadTexture(ToonDNA.GirlBottoms[0][0])
            bottomTex.setMinfilter(Texture.FTLinearMipmapLinear)
            bottomTex.setMagfilter(Texture.FTLinear)
            try:
                bottomColor = ToonDNA.ClothesColors[self.style.botTexColor]
            except:
                bottomColor = ToonDNA.ClothesColors[0]

            darkBottomColor = bottomColor * 0.5
            darkBottomColor.setW(1.0)
            for lodName in self.getLODNames():
                thisPart = self.getPart('torso', lodName)
                top = thisPart.find('**/torso-top')
                top.setTexture(shirtTex, 1)
                top.setColor(shirtColor)
                sleeves = thisPart.find('**/sleeves')
                sleeves.setTexture(sleeveTex, 1)
                sleeves.setColor(sleeveColor)
                bottoms = thisPart.findAllMatches('**/torso-bot')
                for bottomNum in xrange(0, bottoms.getNumPaths()):
                    bottom = bottoms.getPath(bottomNum)
                    bottom.setTexture(bottomTex, 1)
                    bottom.setColor(bottomColor)

                caps = thisPart.findAllMatches('**/torso-bot-cap')
                caps.setColor(darkBottomColor)

        return swappedTorso


    def getDialogueArray(self):
        animalType = self.style.getType()
        if animalType == 'dog':
            dialogueArray = DogDialogueArray
        elif animalType == 'cat':
            dialogueArray = CatDialogueArray
        elif animalType == 'horse':
            dialogueArray = HorseDialogueArray
        elif animalType == 'mouse':
            dialogueArray = MouseDialogueArray
        elif animalType == 'rabbit':
            dialogueArray = RabbitDialogueArray
        elif animalType == 'duck':
            dialogueArray = DuckDialogueArray
        elif animalType == 'monkey':
            dialogueArray = MonkeyDialogueArray
        elif animalType == 'bear':
            dialogueArray = BearDialogueArray
        elif animalType == 'pig':
            dialogueArray = PigDialogueArray
        else:
            dialogueArray = None
        return dialogueArray

    def findSomethingToLookAt(self):
        if self.randGen.random() < 0.1 or not hasattr(self, 'cr'):
            x = self.randGen.choice((-0.8,
             -0.5,
             0,
             0.5,
             0.8))
            y = self.randGen.choice((-0.5,
             0,
             0.5,
             0.8))
            self.lerpLookAt(Point3(x, 1.5, y), blink=1)
            return
        nodePathList = []
        for id, obj in self.cr.doId2do.items():
            if hasattr(obj, 'getStareAtNodeAndOffset') and obj != self:
                node, offset = obj.getStareAtNodeAndOffset()
                if node.getY(self) > 0.0:
                    nodePathList.append((node, offset))

        if nodePathList:
            nodePathList.sort(lambda x, y: cmp(x[0].getDistance(self), y[0].getDistance(self)))
            if len(nodePathList) >= 2:
                if self.randGen.random() < 0.9:
                    chosenNodePath = nodePathList[0]
                else:
                    chosenNodePath = nodePathList[1]
            else:
                chosenNodePath = nodePathList[0]
            self.lerpLookAt(chosenNodePath[0].getPos(self), blink=1)
        else:
            ToonHead.findSomethingToLookAt(self)

    def setupPickTrigger(self):
        Avatar.Avatar.setupPickTrigger(self)
        torso = self.getPart('torso', '1000')
        if torso == None:
            return 0
        self.pickTriggerNp.reparentTo(torso)
        size = self.style.getTorsoSize()
        if size == 'short':
            self.pickTriggerNp.setPosHprScale(0, 0, 0.5, 0, 0, 0, 1.5, 1.5, 2)
        elif size == 'medium':
            self.pickTriggerNp.setPosHprScale(0, 0, 0.5, 0, 0, 0, 1, 1, 2)
        else:
            self.pickTriggerNp.setPosHprScale(0, 0, 1, 0, 0, 0, 1, 1, 2)
        return 1

    def enterNeutral(self, animMultiplier = 1, ts = 0, callback = None, extraArgs = []):
        anim = 'neutral'
        self.pose(anim, int(self.getNumFrames(anim) * self.randGen.random()))
        self.loop(anim, restart=0)
        self.setPlayRate(animMultiplier, anim)
        self.playingAnim = anim
        self.setActiveShadow(1)

    def exitNeutral(self):
        self.stop()

    def enterOff(self, animMultiplier=1, ts=0, callback=None):
        self.playingAnim = None
        return

    def exitOff(self):
        pass


    def __returnToLastAnim(self, task):
        if self.playingAnim:
            self.loop(self.playingAnim)
        elif self.hp > 0:
            self.loop('neutral')
        else:
            self.loop('sad-neutral')
        return Task.done


    def getPieces(self, *pieces):
        results = []
        for lodName in self.getLODNames():
            for partName, pieceNames in pieces:
                part = self.getPart(partName, lodName)
                if part:
                    if type(pieceNames) == types.StringType:
                        pieceNames = (pieceNames,)
                    for pieceName in pieceNames:
                        npc = part.findAllMatches('**/%s;+s' % pieceName)
                        for i in xrange(npc.getNumPaths()):
                            results.append(npc[i])

        return results

    def __doHeadScale(self, scale, lerpTime):
        if scale == None:
            scale = ToontownGlobals.toonHeadScales[self.style.getAnimal()]
        track = Parallel()
        for hi in xrange(self.headParts.getNumPaths()):
            head = self.headParts[hi]
            track.append(LerpScaleInterval(head, lerpTime, scale, blendType='easeInOut'))

        return track

    def __doLegsScale(self, scale, lerpTime):
        if scale == None:
            scale = 1
            invScale = 1
        else:
            invScale = 1.0 / scale
        track = Parallel()
        for li in xrange(self.legsParts.getNumPaths()):
            legs = self.legsParts[li]
            torso = self.torsoParts[li]
            track.append(LerpScaleInterval(legs, lerpTime, scale, blendType='easeInOut'))
            track.append(LerpScaleInterval(torso, lerpTime, invScale, blendType='easeInOut'))

        return track

    def __doToonScale(self, scale, lerpTime):
        if scale == None:
            scale = 1
        node = self.getGeomNode().getChild(0)
        track = Sequence(Parallel(LerpHprInterval(node, lerpTime, Vec3(0.0, 0.0, 0.0), blendType='easeInOut'), LerpScaleInterval(node, lerpTime, scale, blendType='easeInOut')), Func(self.resetHeight))
        return track

    def doToonColorScale(self, scale, lerpTime, keepDefault = 0):
        if keepDefault:
            self.defaultColorScale = scale
        if scale == None:
            scale = VBase4(1, 1, 1, 1)
        node = self.getGeomNode()
        caps = self.getPieces(('torso', 'torso-bot-cap'))
        track = Sequence()
        track.append(Func(node.setTransparency, 1))
        if scale[3] != 1:
            for cap in caps:
                track.append(HideInterval(cap))

        track.append(LerpColorScaleInterval(node, lerpTime, scale, blendType='easeInOut'))
        if scale[3] == 1:
            track.append(Func(node.clearTransparency))
            for cap in caps:
                track.append(ShowInterval(cap))

        elif scale[3] == 0:
            track.append(Func(node.clearTransparency))
        return track


    def __colorToonSkin(self, color, lerpTime):
        track = Sequence()
        colorTrack = Parallel()
        torsoPieces = self.getPieces(('torso', ('arms', 'neck')))
        legPieces = self.getPieces(('legs', ('legs', 'feet')))
        headPieces = self.getPieces(('head', '*head*'))
        if color == None:
            armColor = self.style.getArmColor()
            legColor = self.style.getLegColor()
            headColor = self.style.getHeadColor()
        else:
            armColor = color
            legColor = color
            headColor = color
        for piece in torsoPieces:
            colorTrack.append(Func(piece.setColor, *armColor))

        for piece in legPieces:
            colorTrack.append(Func(piece.setColor, *legColor))

        for piece in headPieces:
            if 'hatNode' not in str(piece) and 'glassesNode' not in str(piece):
                colorTrack.append(Func(piece.setColor, *headColor))

        track.append(colorTrack)
        return track

    def __colorToonEars(self, color, colorScale, lerpTime):
        track = Sequence()
        earPieces = self.getPieces(('head', '*ear*'))
        if len(earPieces) == 0:
            return track
        colorTrack = Parallel()
        if earPieces[0].hasColor():
            if color == None:
                headColor = self.style.getHeadColor()
            else:
                headColor = color
            for piece in earPieces:
                colorTrack.append(Func(piece.setColor, *headColor))

        else:
            if colorScale == None:
                colorScale = VBase4(1, 1, 1, 1)
            for piece in earPieces:
                colorTrack.append(Func(piece.setColorScale, *colorScale))

        track.append(colorTrack)
        return track

    def __colorScaleToonMuzzle(self, scale, lerpTime):
        track = Sequence()
        colorTrack = Parallel()
        muzzlePieces = self.getPieces(('head', '*muzzle*'))
        if scale == None:
            scale = VBase4(1, 1, 1, 1)
        for piece in muzzlePieces:
            colorTrack.append(Func(piece.setColorScale, scale))

        track.append(colorTrack)
        return track

    def __colorToonGloves(self, color, lerpTime):
        track = Sequence()
        colorTrack = Parallel()
        glovePieces = self.getPieces(('torso', '*hands*'))
        if color == None:
            for piece in glovePieces:
                colorTrack.append(Func(piece.clearColor))

        else:
            for piece in glovePieces:
                colorTrack.append(Func(piece.setColor, color))

        track.append(colorTrack)
        return track

    def restoreDefaultColorScale(self):
        node = self.getGeomNode()
        if node:
            if self.defaultColorScale:
                node.setColorScale(self.defaultColorScale)
                if self.defaultColorScale[3] != 1:
                    node.setTransparency(1)
                else:
                    node.clearTransparency()
            else:
                node.clearColorScale()
                node.clearTransparency()

    def __doToonColor(self, color, lerpTime):
        node = self.getGeomNode()
        if color == None:
            return Func(node.clearColor)
        else:
            return Func(node.setColor, color, 1)
        return

    def __doPartsColorScale(self, scale, lerpTime):
        if scale == None:
            scale = VBase4(1, 1, 1, 1)
        node = self.getGeomNode()
        pieces = self.getPieces(('torso', ('arms', 'neck')), ('legs', ('legs', 'feet')), ('head', '+GeomNode'))
        track = Sequence()
        track.append(Func(node.setTransparency, 1))
        for piece in pieces:
            if piece.getName()[:7] == 'muzzle-' and piece.getName()[-8:] != '-neutral':
                continue
            track.append(ShowInterval(piece))

        p1 = Parallel()
        for piece in pieces:
            if piece.getName()[:7] == 'muzzle-' and piece.getName()[-8:] != '-neutral':
                continue
            p1.append(LerpColorScaleInterval(piece, lerpTime, scale, blendType='easeInOut'))

        track.append(p1)
        if scale[3] == 1:
            track.append(Func(node.clearTransparency))
        elif scale[3] == 0:
            track.append(Func(node.clearTransparency))
            for piece in pieces:
                if piece.getName()[:7] == 'muzzle-' and piece.getName()[-8:] != '-neutral':
                    continue
                track.append(HideInterval(piece))

        self.generateHat()
        self.generateGlasses()
        return track



    def putOnSuit(self, suitType, setDisplayName = True, rental = False):
        if self.isDisguised:
            self.takeOffSuit()
        from toontown.suit import Suit
        deptIndex = suitType
        suit = Suit.Suit()
        dna = SuitDNA.SuitDNA()
        if rental == True:
            if SuitDNA.suitDepts[deptIndex] == 's':
                suitType = 'cc'
            elif SuitDNA.suitDepts[deptIndex] == 'm':
                suitType = 'sc'
            elif SuitDNA.suitDepts[deptIndex] == 'l':
                suitType = 'bf'
            elif SuitDNA.suitDepts[deptIndex] == 'c':
                suitType = 'f'
            else:
                self.notify.warning('Suspicious: Incorrect rental suit department requested')
                suitType = 'cc'
        dna.newSuit(suitType)
        suit.setStyle(dna)
        suit.isDisguised = 1
        suit.generateSuit()
        suit.initializeDropShadow()
        suit.setPos(self.getPos())
        suit.setHpr(self.getHpr())
        for part in suit.getHeadParts():
            part.hide()

        suitHeadNull = suit.find('**/joint_head')
        toonHead = self.getPart('head', '1000')
        Emote.globalEmote.disableAll(self)
        toonGeom = self.getGeomNode()
        toonGeom.hide()
        worldScale = toonHead.getScale(render)
        self.headOrigScale = toonHead.getScale()
        headPosNode = hidden.attachNewNode('headPos')
        toonHead.reparentTo(headPosNode)
        toonHead.setPos(0, 0, 0.2)
        headPosNode.reparentTo(suitHeadNull)
        headPosNode.setScale(render, worldScale)
        suitGeom = suit.getGeomNode()
        suitGeom.reparentTo(self)
        if rental == True:
            suit.makeRentalSuit(SuitDNA.suitDepts[deptIndex])
        self.suit = suit
        self.suitGeom = suitGeom
        self.setHeight(suit.getHeight())
        self.nametag3d.setPos(0, 0, self.height + 1.3)
        self.suit.loop('neutral')
        self.isDisguised = 1
        self.setFont(ToontownGlobals.getSuitFont())
        self.nametag.setSpeechFont(ToontownGlobals.getSuitFont())
        if setDisplayName:
            if hasattr(base, 'idTags') and base.idTags:
                name = self.getAvIdName()
            else:
                name = self.getName()
            suitDept = SuitDNA.suitDepts.index(SuitDNA.getSuitDept(suitType))
            suitName = SuitBattleGlobals.SuitAttributes[suitType]['name']
            self.nametag.setDisplayName(TTLocalizer.SuitBaseNameWithLevel % {'name': name,
             'dept': suitName,
             'level': self.cogLevels[suitDept] + 1})
            self.nametag.setWordwrap(9.0)

    def takeOffSuit(self):
        if not self.isDisguised:
            return
        suitType = self.suit.style.name
        toonHeadNull = self.find('**/1000/**/def_head')
        if not toonHeadNull:
            toonHeadNull = self.find('**/1000/**/joint_head')
        toonHead = self.getPart('head', '1000')
        toonHead.reparentTo(toonHeadNull)
        toonHead.setScale(self.headOrigScale)
        toonHead.setPos(0, 0, 0)
        headPosNode = self.suitGeom.find('**/headPos')
        headPosNode.removeNode()
        self.suitGeom.reparentTo(self.suit)
        self.resetHeight()
        self.nametag3d.setPos(0, 0, self.height + 0.5)
        toonGeom = self.getGeomNode()
        toonGeom.show()
        Emote.globalEmote.releaseAll(self)
        self.isDisguised = 0
        self.setFont(ToontownGlobals.getToonFont())
        self.nametag.setSpeechFont(ToontownGlobals.getToonFont())
        self.nametag.setWordwrap(None)
        if hasattr(base, 'idTags') and base.idTags:
            name = self.getAvIdName()
        else:
            name = self.getName()
        self.setDisplayName(name)
        self.suit.delete()
        del self.suit
        del self.suitGeom

    def makeWaiter(self):
        if not self.isDisguised:
            return
        self.suit.makeWaiter(self.suitGeom)



compileGlobalAnimList()

