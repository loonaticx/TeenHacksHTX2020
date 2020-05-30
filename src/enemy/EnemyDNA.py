from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
import random

notify = directNotify.newCategory('EnemyDNA')

enemyHeadTypes = ['f',
 'p',
 'ym',
 'mm',
 'ds',
 'hh',
 'cr',
 'tbc',
 'bf',
 'b',
 'dt',
 'ac',
 'bs',
 'sd',
 'le',
 'bw',
 'sc',
 'pp',
 'tw',
 'bc',
 'nc',
 'mb',
 'ls',
 'rb',
 'cc',
 'tm',
 'nd',
 'gh',
 'ms',
 'tf',
 'm',
 'mh']
enemyATypes = ['ym',
 'hh',
 'tbc',
 'dt',
 'bs',
 'le',
 'bw',
 'pp',
 'nc',
 'rb',
 'nd',
 'tf',
 'm',
 'mh']
enemyBTypes = ['p',
 'ds',
 'b',
 'ac',
 'sd',
 'bc',
 'ls',
 'tm',
 'ms']
enemyCTypes = ['f',
 'mm',
 'cr',
 'bf',
 'sc',
 'tw',
 'mb',
 'cc',
 'gh']
enemyDepts = ['c',
 'l',
 'm',
 's']

enemyDeptFilenames = {'c': 'boss',
 'l': 'law',
 'm': 'cash',
 's': 'sell'
}
enemyDeptModelPaths = {'c': '**/CorpIcon',
 0: '**/CorpIcon',
 'l': '**/LegalIcon',
 1: '**/LegalIcon',
 'm': '**/MoneyIcon',
 2: '**/MoneyIcon',
 's': '**/SalesIcon',
 3: '**/SalesIcon'}
corpPolyColor = VBase4(0.95, 0.75, 0.75, 1.0)
legalPolyColor = VBase4(0.75, 0.75, 0.95, 1.0)
moneyPolyColor = VBase4(0.65, 0.95, 0.85, 1.0)
salesPolyColor = VBase4(0.95, 0.75, 0.95, 1.0)
enemiesPerLevel = [1,
 1,
 1,
 1,
 1,
 1,
 1,
 1]
enemiesPerDept = 8

def getEnemyBodyType(name):
    if name in enemyATypes:
        return 'a'
    elif name in enemyBTypes:
        return 'b'
    elif name in enemyCTypes:
        return 'c'


def getEnemyDept(name):
    index = enemyHeadTypes.index(name)
    if index < enemiesPerDept:
        return enemyDepts[0]
    elif index < enemiesPerDept * 2:
        return enemyDepts[1]
    elif index < enemiesPerDept * 3:
        return enemyDepts[2]
    elif index < enemiesPerDept * 4:
        return enemyDepts[3]



def getEnemyType(name):
    index = enemyHeadTypes.index(name)
    return index % enemiesPerDept + 1


def getEnemyName(deptIndex, typeIndex):
    return enemyHeadTypes[(enemiesPerDept*deptIndex) + typeIndex]


def getRandomEnemyType(level, rng = random):
    return random.randint(max(level - 4, 1), min(level, 8))


def getRandomEnemyByDept(dept):
    deptNumber = enemyDepts.index(dept)
    return enemyHeadTypes[enemiesPerDept * deptNumber + random.randint(0, 7)]

def getEnemiesInDept(dept):
    start = dept * enemiesPerDept
    end = start + enemiesPerDept
    return enemyHeadTypes[start:end]



class EnemyDNA:

    def __init__(self):
        self.newEnemy()

    def __str__(self):
        return 'body = %s, dept = %s, name = %s' % (self.body, self.dept, self.name)

    def __defaultEnemy(self):
        self.name = 'ds'
        self.dept = getEnemyDept(self.name)
        self.body = getEnemyBodyType(self.name)

    def newEnemy(self, name = None):
        if name == None:
            self.__defaultEnemy()
        else:
            self.name = name
            self.dept = getEnemyDept(self.name)
            self.body = getEnemyBodyType(self.name)

    def newEnemyRandom(self, level = None, dept = None):
        self.type = 's'

        if level == None:
            level = random.choice(range(1, len(enemiesPerLevel)))
        elif level < 0 or level > len(enemiesPerLevel):
            notify.error('Invalid enemy level: %d' % level)

        if dept == None:
            dept = random.choice(enemyDepts)

        self.dept = dept
        index = enemyDepts.index(dept)
        base = index * enemiesPerDept
        offset = 0

        if level > 1:
            for i in range(1, level):
                offset = offset + enemiesPerLevel[i - 1]

        bottom = base + offset
        top = bottom + enemiesPerLevel[level - 1]
        self.name = enemyHeadTypes[random.choice(range(bottom, top))]
        self.body = getEnemyBodyType(self.name)
