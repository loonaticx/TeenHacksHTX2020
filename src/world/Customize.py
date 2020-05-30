from panda3d.core import Fog
from direct.gui.DirectScrolledList import DirectScrolledList, DirectButton
from direct.interval.FunctionInterval import Func
from direct.interval.MetaInterval import Sequence
from direct.showbase.ShowBase import Point3
from src.scenefx import EffectsManager
from src.actor import ActorManager

#ideas for changing torso:
#for *each* file(texture) in directory(shirts), add each element into shirtList arr. do the same with pants, sleeve, etc
#and then do a texture flip 180 degrees, attach texture to corresponding nodes, maybe a directScrollList might work..

graphicShaders = EffectsManager
class Customize():
    def __init__(self):
        self.objectList = list()
        self.actor = ActorManager
        pass

    def testCogHeadsHere(self):
        modelArrTwo = ['phase_4/models/char/suitA-heads.bam']
        for modelName in modelArrTwo:
            tempLoader = loader.loadModel(modelName)
            for node in tempLoader.nodes:
                print(node)
        print(self.testTwo.nodes)
        print(self.testTwo.ancestors)
        print(self.testTwo.children)
        print(self.testTwo.findAllMaterials())
        print(self.testTwo.getNodes())

    def annoyingTempHeadList(self):
        backstabber = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/backstabber')
        bigcheese = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/bigcheese')
        bigwig = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/bigwig')
        return [backstabber, bigcheese, bigwig]


    def loadScene(self):
        # Setting up the camera...
        # This is a weird implementation, but it works!
        self.camera = base.camera
        self.secretCamera = loader.loadModel('phase_4/models/props/snowball.bam')
        self.secretCamera.reparentTo(render)
        self.camera.setPos(0, 0, 0)
        self.secretCamera.setPos(self.camera.getPos())
        self.secretCamera.hide()
        self.camera.reparentTo(self.secretCamera)
        # self.camInterval(self.camera)

        # Loading the background
        self.environ = self.loadWorld()

        # Setting up the actor
        self.ourActor = self.actor.makeActor()
        self.ourActor.reparentTo(render)
        self.ourActor.setPos(self.environ.getPos(self.environ.find('**/ground')))

        #EffectsManager.loadFog(7)
        self.loadFog()
        self.camInterval(self.secretCamera, self.ourActor)

        #self.objectList = list()
        #self.objectList.append(actorHead)

    def loadFog(self):
        fog = Fog('distanceFog')
        fog.setColor(0, 0, 0)
        fog.setExpDensity(.07)
        render.setFog(fog)
        fog.setOverallHidden(False)
        return fog.getExpDensity()

    def loadWorld(self):
        background = loader.loadModel('phase_4/models/minigames/treehouse_2players.bam')
        background.reparentTo(render)
        background.setPosHprScale(0.00, 15.00, -3.00, 0.00, 270.00, 180.00, 1.00, 1.00, 1.00)
        return background

    def camInterval(self, cam, actor):
        inc = cam.getX(), cam.getY() + 10, cam.getZ()
        #print(inc)
        #maybe a list of numbers-- an array for x, y, z, a method (manX, manY, manZ) man = manipulate by +- int, ret that array which will be used
        #as the Point3 args. if args are NaN/0/null, just ret the xyz arr. will be used to get the last position args for after the sequence finalizes.
        intervalOne = cam.posInterval(4.0, Point3(inc))
        camSequence = Sequence(intervalOne)
        camSequence.append(Func(self.loadButtons, actor))

        #print(camSequence.__len__())

        camSequence.start()
        #cam.setPos(inc)
        #print ('Pos after interval: ' + str(cam.getPos()))

        #return cam.setPos(cam.getPos())

        #so apparently with the test model it doesn't revert back to 0,0,0
        #just for now, should change later.
        #cam.setPos(cam.getX(), cam.getY() + 10, cam.getZ())

        #if i wanted to make the model change for example during the interval, i could do an event https://www.panda3d.org/manual/?title=Event_Handlers

    def loadButtons(self, actor):
        #arrowUp = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam').find('**/nextUp')
        #arrowDown = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam').find('**/nextDown')
        Button_Up = loader.loadModel('phase_3/models/gui/quit_button.bam').find('**/QuitBtn_UP')
        Button_Down = loader.loadModel('phase_3/models/gui/quit_button.bam').find('**/QuitBtn_DN')
        Button_Rlvr = loader.loadModel('phase_3/models/gui/quit_button.bam').find('**/QuitBtn_RLVR')
        # https://pastebin.com/agdb8260

        Arrow_Up = loader.loadModel('phase_3/models/gui/nameshop_gui.bam').find('**/triangleButtonUp')
        Arrow_Down = loader.loadModel('phase_3/models/gui/nameshop_gui.bam').find('**/triangleButtonDwn')
        Arrow_Rlvr = loader.loadModel('phase_3/models/gui/nameshop_gui.bam').find('**/triangleButtonRllvr')
        Buttons = [Button_Up, Button_Down, Button_Rlvr]

        numItemsVisible = 4
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.54),
            decButton_text_scale=0.04,
            decButton_relief=None,
            decButton_image=(Arrow_Up, Arrow_Down, Arrow_Rlvr),

            incButton_pos=(0.35, 0, -0.01),
            incButton_hpr=(0, 0, 180),
            incButton_text_scale=0.04,
            incButton_relief=None,
            incButton_image=(Arrow_Up, Arrow_Down, Arrow_Rlvr),

            pos=(0.74, 0, 0.4),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_pos=(0.35, 0, 0.43))

        modelArray = ['phase_4/models/neighborhoods/toontown_central.bam',
                      'phase_13/models/parties/partyGrounds.bam',
                      'models/world.egg.pz']
        nameArray = ['Head 1', 'Head 2', 'Head 3']

        thisIsTemp = self.annoyingTempHeadList()

        #for each model in modelArray --> for each node in nodePath, append to array

        for index, name in enumerate(nameArray):
            l = DirectButton(text=name, image=(Buttons), extraArgs=[actor, thisIsTemp[index]], command=changeHead,
                             text_scale=0.045, text_pos=(0, -0.007, 0), relief=None)
            myScrolledList.addItem(l)

    def changeHead(self, ourActor, modelName):
        #if spawned object already exists, we're gonna need to remove it
        while len(self.objectList) >= 1:
            for head in self.objectList:
                head.detachNode()
            self.objectList.pop(0)

        spawnedObject = modelName
        #spawnedObject = loader.loadModel(modelName)
        spawnedObject.reparentTo(self.ourActor.find('**/to_head'))
        spawnedObject.setZ(0.05)
        #eventually havea task to be able to rotate the head around

        #spawnedObject = scene
        #removeWorld(self.objectList.find(spawnedObject))
        self.objectList.append(spawnedObject)
        #print("Model Name: " + repr(modelName))
        #print("Spawned Object: " + repr(spawnedObject))
        testobjectindex = len(self.objectList)
        #print(testobjectindex)
        #print(self.objectList)
