from direct.gui import DirectGuiGlobals
from direct.showbase.ShowBase import ShowBase, loadPrcFile
from src.gamebase import GameGlobals
from src.world import GlobalArena
import builtins

if __dev__:
    loadPrcFile('../config/Config.prc')

class StudioArena(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        DirectGuiGlobals.setDefaultFont(loader.loadFont(GameGlobals.InterfaceFont))
        base.enableParticles()
        self.accept('f4', base.oobe)
        base.disableMouse()

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

        self.arena = GlobalArena.GlobalArena(self)
        self.arena.load()

builtins.base = StudioArena()
base.run()