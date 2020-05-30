from panda3d.core import PlaneNode, NodePath, TextNode, Plane

from direct.gui.DirectLabel import DirectLabel, DirectFrame
from direct.showbase.ShowBaseGlobal import aspect2d
from src.actor import ToonDNA, Toon, ToonHead
from src.gamebase import TheGloriousGameLocalizer, GameGlobals

DialogueTitleText = 0.11
DialogueTitleTextPos = (-0.046, 0.2, 0.092)
DialogueplayButton = 0.055
DialogueinstructionsText = 0.07
DialogueinstructionsTextWordwrap = 26.5
DialogueinstructionsTextPos = (-0.115, 0.05, 0)

class Dialogue:

    def __init__(self, base):
        self.base = base
        pass

    def load(self):
        backgroundGui = loader.loadModel('phase_5/models/cogdominium/tt_m_gui_csa_flyThru.bam')
        self.bg = backgroundGui.find('**/background')
        self.chatBubble = backgroundGui.find('**/chatBubble')
        self.chatBubble.setScale(6.5, 6.5, 7.3)
        self.chatBubble.setPos(0.32, 0, -0.78)
        self.chatBubble.reparentTo(aspect2d)
        self.frame = DirectFrame(geom=self.bg, relief=None, pos=(0.2, 0, -0.6667))
        self.gameTitleText = DirectLabel(parent=self.frame, text=TheGloriousGameLocalizer.ArenaGameTitle,
                                         scale=1, text_align=TextNode.ACenter,
                                         text_fg=(1.0, 0.33, 0.33, 1.0),
                                         pos=DialogueTitleTextPos, relief=None)
        self.chatBubble.wrtReparentTo(self.frame)
        self.frame.hide()

        self.FlippyToon = ToonDNA.ToonDNA('flippy')
        self.FlippyToon.createFlippy()
        Toon.loadModels()
        ToonHead.preloadToonHeads()
        self.toonHead = Toon.Toon()
        #self.toonHead.preloadToonHeads()
        self.toonHead.generateToon()
        #self.makeSuit('bw')
        self.toonHead.getGeomNode().setDepthWrite(1)
        self.toonHead.getGeomNode().setDepthTest(1)
        self.toonHead.loop('neutral')
        self.toonHead.setPosHprScale(-0.73, 0, -1.27, 180, 0, 0, 0.18, 0.18, 0.18)
        self.toonHead.reparentTo(hidden)
        self.toonHead.startBlink()
        self.clipPlane = self.toonHead.attachNewNode(PlaneNode('clip'))
        self.clipPlane.node().setPlane(Plane(0, 0, 1, 0))
        self.clipPlane.setPos(0, 0, 2.45)

        self._toonDialogueSfx = loader.loadSfx('phase_3.5/audio/dial/AV_dog_long.ogg')
        self._camHelperNode = NodePath('CamHelperNode')
        self._camHelperNode.reparentTo(render)
        #dialogue = TTLocalizer.CogdoBarrelRoomIntroDialog
        # CogdoBarrelRoomIntroDialog = 'Good work, Toons! You have haulted the Stomp-O-Matic and are now able to collect some of the stolen Laff barrels, but make sure to hurry before the Cogs come!'