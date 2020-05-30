from panda3d.core import *
import random

class EnemyGrid(object):

    def __init__(self, startX, startY, z, xIncrement, yIncrement, xSize, ySize):
        self.positions = []
        self.occupied = []
        self.xSize = xSize
        self.ySize = ySize

        for i in range(xSize):
            self.positions.append([Vec3(startX + (i * xIncrement), startY + (j * yIncrement), z) for j in range(ySize)])
            self.occupied.append([None for j in range(ySize)])

    def getMaxEnemies(self):
        return self.xSize * self.ySize

    def occupyRandomSpot(self, token):
        for y in range(self.ySize - 1, -1, -1): # Reverse Y loop
            freeIndices = [x for x in range(0, self.xSize) if self.occupied[x][y] is None]

            if freeIndices:
                x = random.choice(freeIndices)
                self.occupied[x][y] = token
                return self.positions[x][y]

    def releaseSpot(self, token):
        for x in range(0, self.xSize):
            for y in range(0, self.ySize):
                if self.occupied[x][y] == token:
                    self.occupied[x][y] = None