from panda3d.core import Fog

class FogManager():
    def __init__(self):
        pass

    def loadFog(self, fogDensity):
        fog = Fog('distanceFog')
        fog.setColor(0, 0, 0)
        fog.setExpDensity(fogDensity * (math.pow(10, -2)))
        render.setFog(fog)
        fog.setOverallHidden(False)
        #fog.getExpDensity()
        print(fog.getExpDensity())
        print("tried to load fog")
        return fog
