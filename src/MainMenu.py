import os
from direct.gui import DirectGuiGlobals
from direct.gui.DirectButton import DirectButton
from direct.gui.OnscreenImage import OnscreenImage, TransparencyAttrib
from direct.showbase.ShowBase import ShowBase, loadPrcFile
from src import ConfigManager
from src.actor import Avatar
from panda3d.core import *

from src.gamebase import GameGlobals

if __debug__:
    loadPrcFile('../config/Config.prc')
    print(os.getcwd())

class MainMenu(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.base = ShowBase
        DirectGuiGlobals.setDefaultFont(loader.loadFont(GameGlobals.InterfaceFont))
        base.enableParticles()
        self.NEWintroButtons()
        #self.config = self.loadConfig()
        #self.debug = self.config["settings"]['want-debug-mode']
        #print(self.debug)
        base.disableMouse()
        self.debug = True

        if self.debug:
            print("Debug mode enabled!")
            self.accept('f4', base.oobe)

            if __debug__:
                try:
                    from src.debug.OTPInjectorDev import Injector
                    self.injector = Injector()
                except ImportError:
                    print("You don't have wxPython or psutil installed.")
                    print("You need them to use the injector!")
                except:
                    import traceback
                    traceback.print_exc()

    def loadConfig(self):
        conf = ConfigManager.ConfigManager()
        conf.generateSettings()
        return conf.loadSettings()



    def cleanupButtons(self):
        self.loadButton.removeNode()
        #self.customizeButton.removeNode()
        #self.arenaButton.destroy()
        self.imageObject.destroy()
        #self.testLoadingScreen.destroy()

    def loadGame(self):
        print("Loading game...")
        from src import FirstPerson
        self.landwalker = FirstPerson.firstPerson(self.win, self.camera)
        #self.landwalker.loadGame()
        self.cleanupButtons()




    def NEWintroButtons(self):
        self.imageObject = OnscreenImage(image='stat_board.png', pos=(0, 0, 0))
        self.imageObject.setTransparency(TransparencyAttrib.MAlpha)

        buttonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.loadButton = DirectButton(frameSize=None, text="Load Game", image=(buttonImage.find('**/QuitBtn_UP'),
                                                                 buttonImage.find('**/QuitBtn_DN'),
                                                                 buttonImage.find('**/QuitBtn_RLVR')),
                               relief=None, command=self.loadGame, text_pos=(0, -0.015),
                               geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, 0.30),
                               text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)
        #self.customizeButton = DirectButton(frameSize=None, text="Customize", image=(buttonImage.find('**/QuitBtn_UP'),
        #                                                         buttonImage.find('**/QuitBtn_DN'),
        #                                                         buttonImage.find('**/QuitBtn_RLVR')),
        #                       relief=None, command=self.loadCustomize, text_pos=(0, -0.015),
        #                       geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, -0.30),
        #                       text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)


    def introButtons(self):
        self.imageObject = OnscreenImage(image='stat_board.png', pos=(0, 0, 0))
        self.imageObject.setTransparency(TransparencyAttrib.MAlpha)

        buttonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.testLoadingScreen = DirectButton(frameSize=None, text="Test Loading Game", image=(buttonImage.find('**/QuitBtn_UP'),
                                                                                buttonImage.find('**/QuitBtn_DN'),
                                                                                buttonImage.find('**/QuitBtn_RLVR')),
                                       relief=None, command=self.loadTest, text_pos=(0, -0.015),
                                       geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, 0.60),
                                       text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)
        self.loadButton = DirectButton(frameSize=None, text="Load Game", image=(buttonImage.find('**/QuitBtn_UP'),
                                                                 buttonImage.find('**/QuitBtn_DN'),
                                                                 buttonImage.find('**/QuitBtn_RLVR')),
                               relief=None, command=self.loadGame, text_pos=(0, -0.015),
                               geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, 0.30),
                               text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)
        self.customizeButton = DirectButton(frameSize=None, text="Customize", image=(buttonImage.find('**/QuitBtn_UP'),
                                                                 buttonImage.find('**/QuitBtn_DN'),
                                                                 buttonImage.find('**/QuitBtn_RLVR')),
                               relief=None, command=self.loadCustomize, text_pos=(0, -0.015),
                               geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, -0.30),
                               text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)
        self.arenaButton = DirectButton(frameSize=None, text="Arena Game", image=(buttonImage.find('**/QuitBtn_UP'),
                                                                 buttonImage.find('**/QuitBtn_DN'),
                                                                 buttonImage.find('**/QuitBtn_RLVR')),
                               relief=None, command=self.loadArena, text_pos=(0, -0.015),
                               geom=None, pad=(0.01, 0.01), suppressKeys=0, pos=(0.00, 0.00, 0),
                               text_scale=0.059999999999999998, borderWidth=(0.015, 0.01), scale=2.53)
        buttonImage.removeNode()


program = MainMenu()
program.run()