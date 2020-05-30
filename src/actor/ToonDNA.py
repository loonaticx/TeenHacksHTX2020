# for dialogue
from src.actor.ActorDict import *


class ToonDNA:

    def __init__(self, type = None):
        self.createFlippy()

    def __str__(self):
        string = 'type = toon\n'
        string = string + 'gender = %s\n' % self.gender
        string = string + 'head = %s, torso = %s, legs = %s\n' % (self.head, self.torso, self.legs)
        string = string + 'arm color = %s\n' % (self.armColor,)
        string = string + 'glove color = %s\n' % (self.gloveColor,)
        string = string + 'leg color = %s\n' % (self.legColor,)
        string = string + 'head color = %s\n' % (self.headColor,)
        string = string + 'top texture = %d\n' % self.topTex
        string = string + 'top texture color = %d\n' % self.topTexColor
        string = string + 'sleeve texture = %d\n' % self.sleeveTex
        string = string + 'sleeve texture color = %d\n' % self.sleeveTexColor
        string = string + 'bottom texture = %d\n' % self.botTex
        string = string + 'bottom texture color = %d\n' % self.botTexColor
        return string



    def createFlippy(self):
        # ('dss', 'ss', 'm', 'm', 2, 0, 2, 2, 1, 8, 1, 8, 1, 14)
        self.type = 't'
        self.head = 'css'
        self.torso = 'ss'
        self.legs = 'm'
        self.gender = 'm'
        self.armColor = 2
        self.gloveColor = 0
        self.legColor = 2
        self.headColor = 2
        self.topTex = 1
        self.topTexColor = 8
        self.sleeveTex = 1
        self.sleeveTexColor = 8
        self.botTex = 1
        self.botTexColor = 14

    def migrateColor(self, color):
        return allColorsList[color] if isinstance(color, int) else color

