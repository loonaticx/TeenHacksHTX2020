
from direct.showbase.DirectObject import DirectObject
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from src.camera import MouseLook


class firstPerson():

    def __init__(self):
        pass

    def __init__(self, win, cam):
        self.loadWorld()
        self.mouseConfig(win, cam)

    def loadWorld(self):
        # Load the environment model.
        self.environ = loader.loadModel("room.egg")
        # Reparent the model to render.
        self.environ.reparentTo(render)
        # Apply scale and position transforms on the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

    def mouseConfig(self, win, cam):
        base.disableMouse()

        self.mouseLook = MouseLook.FirstPersonCamera(win, cam)
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

        if (base.mouseWatcherNode.hasMouse() == True):
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
