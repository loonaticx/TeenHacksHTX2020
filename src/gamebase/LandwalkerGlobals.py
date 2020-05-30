from panda3d.core import TextNode

from direct.gui.OnscreenText import OnscreenText
#from src.actor import LandwalkerAvatarControls


#import ConfigMgr

def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1),
                        parent=base.a2dTopLeft, align=TextNode.ALeft,
                        pos=(0.08, -pos - 0.04), scale=.05)

def setInstructions():
    inst1 = addInstructions(0.06, "Press F to toggle wireframe")
    inst2 = addInstructions(0.12, "Press X to toggle xray")
    inst3 = addInstructions(0.18, "Press 1 to activate cartoon shading")
    inst4 = addInstructions(0.24, "Press 2 to deactivate cartoon shading")
    inst4 = addInstructions(0.30, "Press 3 to toggle fog")
    inst4 = addInstructions(0.36, "Press 4 to toggle free camera")
    inst4 = addInstructions(0.42, "Press 5 to toggle bloom")
    inst4 = addInstructions(0.48, "Press 6 to toggle Ambient Occlusion")
    inst4 = addInstructions(0.54, "Press Escape to toggle the onscreen debug")

#direct.showbase.Messenger.Messenger.accept()

AOEnabled = False
bloomEnabled = False
invertEnabled = False
OSD = True
shadersLoaded = False
xray_mode = False
show_model_bounds = False
fogEnabled = True
mouseEnabled = False

LandWalkerFog = 1.0
CustomizeAreaFog = 7.0

# Store which keys are currently pressed
keyMap = {
    "1": 0,
    "escape": 0,
    "left": 0,
    "right": 0,
    "forward": 0,
    "backward": 0,
    "cam-left": 0,
    "cam-right": 0,
}

offset = 3.2375
def setKeys():
    setKey = src.actor.LandwalkerAvatarControls.setKey
    # Accept the control keys for movement and rotation
    #    base.accept('f', toggleWireframe)
    #base.accept('x', EffectsManager.toggle_xray_mode)
    #base.accept('b', toggle_model_bounds)
    #base.accept("escape", toggle_osd)
    #base.accept("1", loadCartoonShaders)
    #base.accept("2", unloadShaders)
    #base.accept("3", EffectsManager.toggleFog()) # fog, fogEnabled, fogDensity
    #base.accept("4", EffectsManager.toggleCamera)
    #base.accept("5", EffectsManager.toggleBloom)
    #base.accept("6", EffectsManager.toggleAmbientOcclusion)
    #warning: bright! accept("6", toggleInvert)
    base.accept("arrow_left", setKey, ["left", True])
    base.accept("arrow_right", setKey, ["right", True])
    base.accept("arrow_up", setKey, ["forward", True])
    base.accept("arrow_down", setKey, ["backward", True])
    base.accept("arrow_left-up", setKey, ["left", False])
    base.accept("arrow_right-up", setKey, ["right", False])
    base.accept("arrow_up-up", setKey, ["forward", False])
    base.accept("arrow_down-up", setKey, ["backward", False])

