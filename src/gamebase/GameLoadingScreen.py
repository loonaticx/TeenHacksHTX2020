from panda3d.core import ConfigVariableDouble, Filename, TransparencyAttrib, Loader, VBase3, TextNode, Vec4

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui import DirectGuiGlobals
from direct.gui.DirectWaitBar import DirectWaitBar
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBaseGlobal import aspect2d
from src.gamebase import GameGlobals

notify = directNotify.newCategory('GameLoadingScreen')
notify.setInfo(True)
LOADING_SCREEN_SORT_INDEX = 4000

class GameLoadingScreen:

    def __init__(self):
        self.GameBackgroundSetup = False

    def SetupGameBackground(self):
        if not self.GameBackgroundSetup:
            self.__count = 0
            self.__expectedCount = range

            notify.info('Starting the game...')
            self.LoadBackground()

            notify.info('Setting the default font...')
            DirectGuiGlobals.setDefaultFontFunc(GameGlobals.InterfaceFont)

            if base.win is None:
                notify.error('Unable to open window; aborting.')
            ConfigVariableDouble('decompressor-step-time').setValue(0.01)
            ConfigVariableDouble('extractor-step-time').setValue(0.01)
            base.graphicsEngine.renderFrame()
            self.LoadGameVersion()
            self.GameBackgroundSetup = True
        pass

    def LoadBackground(self):
        tempLoader = Loader()
        self.backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background.bam'))
        self.backgroundNodePath = aspect2d.attachNewNode(self.backgroundNode)
        self.backgroundNodePath.setPos(0.0, 0.0, 0.0)
        self.backgroundNodePath.setScale(render2d, VBase3(1))
        self.backgroundNodePath.find('**/fg').hide()
        logo = OnscreenImage(
            image='phase_3/maps/tt-logo.png',
            scale=(1 / (4.0 / 3.0), 1, 1 / (4.0 / 3.0)),
            pos=self.backgroundNodePath.find('**/fg').getPos())
        logo.setTransparency(TransparencyAttrib.MAlpha)
        logo.setBin('fixed', 20)
        logo.reparentTo(self.backgroundNodePath)
        self.backgroundNodePath.find('**/bg').setBin('fixed', 10)
        self.LoadBar()

    def LoadBar(self):
        self.waitBar = DirectWaitBar(guiId='LoadingScreenWaitBar', parent=self.backgroundNodePath, frameSize=(
            base.a2dLeft + (base.a2dRight / 4.95), base.a2dRight - (base.a2dRight / 4.95), -0.03, 0.03),
                                     pos=(0, 0, 0.15),
                                     text='')

        self.waitBar['frameSize'] = (
            base.a2dLeft + (base.a2dRight / 4.95), base.a2dRight - (base.a2dRight / 4.95), -0.03, 0.03)
        self.waitBar.reparentTo(base.a2dpBottomCenter, LOADING_SCREEN_SORT_INDEX)
        self.waitBar.update(self.__count)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)

    def LoadGameVersion(self):
        # GameVersion = base.config.GetString('server-version', 'no_version_set')
        GameVersion = 'Early Development Build'
        version = OnscreenText(GameVersion, pos=(-1.3, -0.975), scale=0.06, fg=Vec4(0, 0, 1, 0.6),
                               align=TextNode.ALeft)
        version.setPos(0.03, 0.03)
        version.reparentTo(base.a2dBottomLeft)


