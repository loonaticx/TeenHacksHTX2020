from direct.gui import DirectGuiGlobals
from direct.gui.DirectButton import DirectButton
from direct.gui.OnscreenImage import OnscreenImage, TransparencyAttrib
from direct.showbase.ShowBase import ShowBase, loadPrcFile, NodePath, PandaNode
from src.battle import DirectCannon
from src.gamebase import GameGlobals
from src.world import GlobalArena

if __dev__:
    loadPrcFile('../config/Config.prc')

class Studio(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.game = GlobalArena.GlobalArena(self)
        self.loadCamera()
        self.game.showCrosshair()

        self.loadBackground()
        self.loadCannon()

    def loadCamera(self):
        # Setting up the camera...
        # This is a weird implementation, but it works!
        self.camera = base.camera
        self.secretCamera = loader.loadModel('phase_4/models/props/snowball.bam')
        self.secretCamera.reparentTo(render)
        self.secretCamera.setPos(self.camera.getPos())
        #self.secretCamera.hide()
        self.camera.reparentTo(self.secretCamera)
        #self.camera.setPosHprScale(91.61, -40.72, 7.13, 15, 0.00, 0.00, 1.00, 1.00, 1.00) # -45.76 one
        self.camera.setPosHprScale(120.00, 20.00, 30.00, 90.00, 342.00, 0.00, 1.00, 1.00, 1.00)
        # camera.setPosHprScale(100.17, -76.31, 13.11, 23.96, 356.82, 0.00, 1.00, 1.00, 1.00)


    def loadBackground(self):
        self.TestPlane = loader.loadModel("planetest.egg")
        self.TestPlane.reparentTo(render)
        self.tempHQ = loader.loadModel('phase_3.5/models/modules/hqTEST2-mod.egg')
        self.tempHQ.reparentTo(render)


    def loadCannon(self):
        self.cannon = DirectCannon.DirectCannon(self)
        self.cannon.load()
        self.cannon.activateCannons()
        self.cannon.enterLoad()

        self.cannon.cannon.reparentTo(self.TestPlane)

app = Studio()
app.run()
