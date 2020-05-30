from src.gamebase import LandwalkerGlobals

keyMap = LandwalkerGlobals.keyMap

def getAirborneHeight():
    return LandwalkerGlobals.offset + 0.025000000000000001

# Records the state of the arrow keys
def setKey(key, value):
    keyMap[key] = value

# Accepts arrow keys to move either the player or the menu cursor,
# Also deals with grid checking and collision detection
def move(task):
    dt = globalClock.getDt()
    if keyMap["forward"]:
            base.localAvatar.setY(base.localAvatar, 20 * dt)
    elif keyMap["backward"]:
            base.localAvatar.setY(base.localAvatar, -20 * dt)
    if keyMap["left"]:
            base.localAvatar.setHpr(base.localAvatar.getH() + 1.5, base.localAvatar.getP(), base.localAvatar.getR())
    elif keyMap["right"]:
            base.localAvatar.setHpr(base.localAvatar.getH() - 1.5, base.localAvatar.getP(), base.localAvatar.getR())

    currentAnim = base.localAvatar.getCurrentAnim()

    if keyMap["forward"]:
        if currentAnim != "walk":
            base.localAvatar.loop("walk")
    elif keyMap["backward"]:
        # Play the walk animation backwards.
        if currentAnim != "walk":
            base.localAvatar.loop("walk")
        base.localAvatar.setPlayRate(-1.0, "walk")
    elif keyMap["left"] or keyMap["right"]:
        if currentAnim != "walk":
            base.localAvatar.loop("walk")
        base.localAvatar.setPlayRate(1.0, "walk")
    else:
        if currentAnim is not None:
            base.localAvatar.stop()
            base.localAvatar.loop("neutral")
            isMoving = False
    return task.cont


