from panda3d.core import *
import colorsys, random, math

def getHeadsUpHpr(fromPos, toPos):
    quat = Quat()
    headsUp(quat, toPos - fromPos, Vec3.up())
    return quat.getHpr()

import colorsys, random, math

def loadGradientTexture(hue, minSat, maxSat, minVal, maxVal):
    image = PNMImage(int((maxSat - minSat) * 100), int((maxVal - minVal) * 100))
    
    for x in range(image.getXSize()):
        for y in range(image.getYSize()):
            image.setXel(x, y, colorsys.hsv_to_rgb(hue, (y / 100.0) + minVal, (x / 100.0) + minSat))
    
    texture = Texture()
    texture.load(image)
    
    return texture

def loadGradient(parent, frame, hue, minSat, maxSat, minVal, maxVal):
    model = loadTextureModel(loadGradientTexture(hue, minSat, maxSat, minVal, maxVal), 'gradient', frame)
    model.reparentTo(parent)
    
    return model

def loadCardModel(name='card', frame=(-1, 1, -1, 1), transparency=False):
    card = CardMaker(name)
    card.setFrame(*frame)
    
    card = NodePath(card.generate())

    if transparency:
        card.setTransparency(True)
    
    return card

def loadTextureModel(texture, name='card', frame=(-1, 1, -1, 1), transparency=False):
    card = loadCardModel(name, frame, transparency)
    card.setTexture(texture, 1)

    return card

def getRandomSatVal(startSat, startVal):
    return startSat + random.uniform(min(1.0 - startSat, 0.1), 1.0 - startSat), startVal + random.uniform(min(1.0 - startVal, 0.1), 1.0 - startVal)

def loadRandomGradient(parent, frame, hue, startSat, startVal):
    maxSat, maxVal = getRandomSatVal(startSat, startVal)

    return loadGradient(parent, frame, hue, startSat, maxSat, startVal, maxVal)
