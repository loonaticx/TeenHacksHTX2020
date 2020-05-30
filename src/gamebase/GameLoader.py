
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase import Loader
from direct.showbase.ShowBaseGlobal import aspect2d, globalClock
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from src.gamebase import GameGlobals, GameLoadingScreen
from src.world import GlobalArena

notify = directNotify.newCategory('GameLoader')
notify.setInfo(True)

Preloaded = {}
class GameLoader(Loader.Loader):
    TickPeriod = 0.2

    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.base = base
        self.inBulkBlock = None
        self.blockName = None
        self.loadingScreen = GameLoadingScreen.GameLoadingScreen()
        self.loadingScreen.SetupGameBackground()
        self.beginBulkLoad('c')
        self.arena = GlobalArena.GlobalArena(self.base)
        #self.arena.load()
        return


    def beginBulkLoad(self, name):
        self._loadStartT = globalClock.getRealTime()
        Loader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return None
        self.inBulkBlock = 1
        self._lastTickT = globalClock.getRealTime()
        self.blockName = name
        #####self.loadingScreen.LoadBackground()

        return None

    def loadModel(self, *args, **kwargs):
        ret = loader.loadModel(self, *args, **kwargs)
        if ret:
            gsg = base.win.getGsg()
            if gsg:
                ret.prepareScene(gsg)
        self.tick()
        return ret

    def tick(self):
        if self.inBulkBlock:
            now = globalClock.getRealTime()
            if now - self._lastTickT > self.TickPeriod:
                self._lastTickT += self.TickPeriod
                self.loadingScreen.tick()
                try:
                    base.cr.considerHeartbeat()
                except:
                    pass

    def destroy(self):
        pass