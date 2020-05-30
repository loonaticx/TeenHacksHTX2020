
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from src.camera import MouseLook
from src.scenefx import EffectsManager

graphicShaders = EffectsManager
class firstPerson():

    def __init__(self):
        pass

    def __init__(self, win, cam):
        self.loadWorld()
        self.mouseConfig(win, cam)
        EffectsManager.loadShaders()

    def loadWorld(self):
        # Load the environment model.
        self.room = loader.loadModel("room.egg")
        # Reparent the model to render.
        self.room.reparentTo(render)

        self.desk = loader.loadModel("CompDesk.egg")
        self.desk.reparentTo(render)

        self.chair = loader.loadModel("deskChair.egg")
        self.chair.reparentTo(render)
        self.chair.setPosHprScale(0.00, -18.85, 0.62, 0.00, 0.00, 0.00, 1.16, 1.16, 1.16)

        self.loadFog()

    def loadFog(self):
        fog = Fog('distanceFog')
        fog.setColor(0, 0, 0)
        fog.setExpDensity(.07)
        render.setFog(fog)
        fog.setOverallHidden(False)
        return fog

    def unloadShaders(self):
        if self.shadersLoaded:
            self.drawnScene.hide()
            self.shadersLoaded = False

    def loadCartoonShaders(self):
        if not self.shadersLoaded:
            separation = 0.0015
            cutoff = 0.35
            inkGen = loader.loadShader("shaders/inkGen.sha")
            self.drawnScene.setShader(inkGen)
            self.drawnScene.setShaderInput("separation", LVecBase4(separation, 0, separation, 0))
            self.drawnScene.setShaderInput("cutoff", LVecBase4(cutoff))
            self.drawnScene.show()
            shadersLoaded = True

    def mouseConfig(self, win, cam):
        base.disableMouse()

        self.mouseLook = MouseLook.FirstPersonCamera(base, cam)
        self.mouseLook.start()
        base.accept("tab", self.mouseLook.start)
        base.accept("escape", self.mouseLook.stop)

