from direct.gui import DirectGuiGlobals
from direct.showbase.ShowBase import ShowBase, loadPrcFile
from src.gamebase import GameGlobals
from src.battle import Dialogue
import builtins

if __debug__:
    loadPrcFile('../config/Config.prc')

class StudioDialogue(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        DirectGuiGlobals.setDefaultFont(loader.loadFont(GameGlobals.InterfaceFont))
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

        self.dia = Dialogue.Dialogue(ShowBase)
        self.dia.load()

builtins.base = StudioDialogue()
base.run()