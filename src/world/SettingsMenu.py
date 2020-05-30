from direct.gui.OnscreenImage import OnscreenImage, TransparencyAttrib


class SettingsMenu:
    def __init__(self):
        pass

    def LoadSettingsGUI(self):
        self.SettingsBackground = OnscreenImage(image='stat_board.png', pos=(0, 0, 0))
        self.SettingsBackground.setTransparency(TransparencyAttrib.MAlpha)

    def ToggleControlScheme(self):
        pass
    # if i can figure how to get custom keybindings to work lol
