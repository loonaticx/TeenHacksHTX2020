
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


class World(DirectObject):
    def setup(self):
        #base = ShowBase()
        #base.__init__(self)
        base.setBackgroundColor(1, 1, 1)
        base.disableMouse()
        self.environmentModel = loader.loadModel("models/environment")
        self.environmentModel.reparentTo(render)
        self.environmentModel.setPos(0, 20, -10)

        self.cameraModel = loader.loadModel("models/camera")
        self.cameraModel.reparentTo(render)
        self.cameraModel.setPos(0, 15, 0)

        base.camera.reparentTo(self.cameraModel)
        base.camera.setY(base.camera, 5)

        self.keyMap = {"w": False, "s": False, "a": False, "d": False, }

        self.accept("w", self.setKey, ["w", True])
        self.accept("s", self.setKey, ["s", True])
        self.accept("a", self.setKey, ["a", True])
        self.accept("d", self.setKey, ["d", True])

        self.accept("w-up", self.setKey, ["w", False])
        self.accept("s-up", self.setKey, ["s", False])
        self.accept("a-up", self.setKey, ["a", False])
        self.accept("d-up", self.setKey, ["d", False])

        taskMgr.add(self.cameraControl, "Camera Control")

    def setKey(self, key, value):
        self.keyMap[key] = value

    def cameraControl(self, task):
        dt = globalClock.getDt()
        if (dt > .20):
            return task.cont

        if (base.mouseWatcherNode.hasMouse()):
            mpos = base.mouseWatcherNode.getMouse()
            base.camera.setP(mpos.getY() * 30)
            base.camera.setH(mpos.getX() * -50)
            if (mpos.getX() < 0.1 and mpos.getX() > -0.1):
                self.cameraModel.setH(self.cameraModel.getH())
            else:
                self.cameraModel.setH(self.cameraModel.getH() + mpos.getX() * -1)

        if (self.keyMap["w"] == True):
            self.cameraModel.setY(self.cameraModel, 15 * dt)
            print("camera moving forward")
            return task.cont
        elif (self.keyMap["s"] == True):
            self.cameraModel.setY(self.cameraModel, -15 * dt)
            print("camera moving backwards")
            return task.cont

#application = firstPerson()

#application.run()
