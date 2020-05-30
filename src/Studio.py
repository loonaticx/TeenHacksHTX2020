from direct.gui import DirectGuiGlobals
from direct.gui.DirectButton import DirectButton
from direct.gui.OnscreenImage import OnscreenImage, TransparencyAttrib
from direct.showbase.ShowBase import ShowBase, loadPrcFile, NodePath, PandaNode

if __debug__:
    loadPrcFile('../config/Config.prc')

class Studio(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.loadCamera()

        self.loadWorld()

    def loadCamera(self):
        self.camera = base.camera
        self.secretCamera = loader.loadModel('models/camera.bam')
        self.secretCamera.reparentTo(render)
        self.secretCamera.setPos(self.camera.getPos())
        #self.secretCamera.hide()
        self.camera.reparentTo(self.secretCamera)
        #self.camera.setPosHprScale(91.61, -40.72, 7.13, 15, 0.00, 0.00, 1.00, 1.00, 1.00) # -45.76 one
        self.camera.setPosHprScale(120.00, 20.00, 30.00, 90.00, 342.00, 0.00, 1.00, 1.00, 1.00)
        # camera.setPosHprScale(100.17, -76.31, 13.11, 23.96, 356.82, 0.00, 1.00, 1.00, 1.00)


    def loadWorld(self):
        # Load the environment model.
        self.room = loader.loadModel("room.egg")
        # Reparent the model to render.
        self.room.reparentTo(render)

        self.desk = loader.loadModel("CompDesk.egg")
        self.desk.reparentTo(render)

        self.chair = loader.loadModel("deskChair.egg")
        self.chair.reparentTo(render)
        self.chair.place()

app = Studio()
app.run()
