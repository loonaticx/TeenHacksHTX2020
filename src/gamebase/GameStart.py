# https://github.com/LittleNed/ToontownStride/blob/master/toontown/toontowngui/ToontownLoadingScreen.py
# https://github.com/LittleNed/ToontownStride/blob/master/toontown/toonbase/ToontownStart.py
# https://github.com/LittleNed/ToontownStride/blob/master/toontown/toonbase/ToontownLoader.py
from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from panda3d.core import *
loadPrcFile('../config/Config.prc')


import time
import sys
import random
from direct.directnotify.DirectNotifyGlobal import directNotify
from src.gamebase import GameLoader
from direct.showbase import Loader

notify = directNotify.newCategory('GameStart')
notify.setInfo(True)


class GameStart:

    def __init__(self, base):
        self.game = GameLoader.GameLoader(base)
        return

    def destroy(self):
        self.loadingScreen.destroy()
        del self.loadingScreen
        Loader.Loader.destroy(self)



#app = GameStart()
#app.run()