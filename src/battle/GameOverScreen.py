from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
from src.gamebase import GameUtils

class GameOverScreen(DirectObject):

    def __init__(self, win):
        self.win = win
        self.hue = 0.33 if win else 0
        self.saturation = 0.5 if win else 0.85
        self.background = None
        self.topLabel = None
        self.bottomLabel = None
        self.button = None

    def load(self):
        self.background = GameUtils.loadRandomGradient(render2d, (-1, 1, -1, 1), self.hue, self.saturation, 0.5)
        self.topLabel = DirectLabel(base.a2dTopCenter, relief=None, text_scale=0.1, text=self.getTopText(), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), pos=(0, 0, -0.25))
        self.bottomLabel = DirectLabel(base.a2dBottomCenter, relief=None, text_scale=0.1, text=self.getBottomText(), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), pos=(0, 0, 0.75))
        
        buttonModel = loader.loadModel('phase_3/models/gui/quit_button')
        yellowButton = [buttonModel.find('**/QuitBtn_' + name) for name in ('UP', 'DN', 'RLVR')]

        self.button = DirectButton(base.a2dBottomCenter, relief=None, image=yellowButton, image_scale=(0.8, 1, 1), text="Let's go!", text_scale=0.055, text_pos=(0, -0.02), text_fg=(0, 0, 0, 1), pos=(0, 0, 0.25), scale=1.6, command=self.restartGame)
        buttonModel.removeNode()
    
    def enter(self):
        base.playMusic(loader.loadMusic(self.getMusic()), looping=True)

    def unload(self):
        if self.background:
            self.background.removeNode()
            self.background = None
        if self.topLabel:
            self.topLabel.removeNode()
            self.topLabel = None
        if self.bottomLabel:
            self.bottomLabel.removeNode()
            self.bottomLabel = None
        if self.button:
            self.button.removeNode()
            self.button = None
    
    def getTopText(self):
        if self.win:
            return 'Woohoo!\n\nThe Suits have been driven back to their factories!\n\nThe Town is safe once again!'
        else:
            return 'Oh no!!!\n\nThe Suits have defeated your Headquarters.\nThe Town is in total disarray...'
    
    def getBottomText(self):
        if self.win:
            return 'But we must call upon your power once again...\n\nWould you like to play again?'
        else:
            return 'Perhaps your light will guide our Town one day...\n\nWould you like to try again?'
    
    def getMusic(self):
        if self.win:
            return 'phase_9/audio/bgm/encntr_hall_of_fame.ogg'
        else:
            return 'phase_9/audio/bgm/encntr_head_suit_theme.ogg'

    def restartGame(self):
        from src.world.GlobalArena import GlobalArena
        self.unload()
        base.arena = GlobalArena(base)
        base.arena.load()