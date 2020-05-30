# https://github.com/LittleNed/ToontownStride/blob/master/toontown/toonbase/TTLocalizerEnglish.py
from pandac.PandaModules import BitMask32, Vec4
from src.gamebase import BitmaskGlobals
#WallBitmask = BitMask32(16)

InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'

CannonAmmo = 12

FUSE_TIME = 0.0
CANNON_TIMEOUT = 30
CANNON_MOVIE_LOAD = 1
CANNON_MOVIE_CLEAR = 2
CANNON_MOVIE_FORCE_EXIT = 3
CANNON_MOVIE_LANDED = 4

AvatarDefaultRadius = 1
EnemyForwardSpeed = 12.0
EnemyTurnSpeed = 60.0

HQLaffPoints = 500
AttackMinHP = 30
AttackMaxHP = 60
IntermissionHealHP = 100

SignFont = None

def getSignFont():
    global SignFont
    if not SignFont:
        SignFont = loader.loadFont('phase_3/models/fonts/MickeyFont.bam', lineHeight=1.0)
    return SignFont