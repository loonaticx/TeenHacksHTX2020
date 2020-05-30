from direct.gui.DirectButton import DirectButton
from direct.gui.OnscreenImage import OnscreenImage
from direct.showbase.ShowBase import ShowBase, DisplayRegion, TransparencyAttrib
from panda3d.core import InputDevice
from src.test import ColorPicker


class TestWorld(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.man = InputDevice.connected
        print(InputDevice.hasFeature(InputDevice.Feature.tracker))

    def NEWintroButtons(self):
        self.imageObject = OnscreenImage(image='stat_board.png', pos=(0, 0, 0))
        self.imageObject.setTransparency(TransparencyAttrib.MAlpha)

        buttonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.loadButton = DirectButton(frameSize=None, text="Load Game", image=(buttonImage.find('**/QuitBtn_UP'),
                                                                 buttonImage.find('**/QuitBtn_DN'),
                                                                 buttonImage.find('**/QuitBtn_RLVR')),
                               relief=None, command=print("gay boy"), text_pos=(0, -0.015),
                               geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, 0.30),
                               text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)
        self.color = ColorPicker.ColorPicker(buttonImage)



app = TestWorld()
app.run()
