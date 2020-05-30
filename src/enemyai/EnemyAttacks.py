from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.actor.Actor import Actor
from src.scenefx import EffectsManager
import random

PNT3_NEARZERO = Point3(0.01, 0.01, 0.01)
PNT3_ZERO = Point3(0.0, 0.0, 0.0)
PNT3_ONE = Point3(1.0, 1.0, 1.0)

def removeProp(prop):
    if prop is None or prop.isEmpty():
        return

    if isinstance(prop, Actor):
        prop.cleanup()
    else:
        prop.removeNode()

def __showProp(prop, parent, pos, hpr = None, scale = None):
    if prop is None or prop.isEmpty():
        return
    if parent is None or parent.isEmpty():
        return
    prop.reparentTo(parent)
    prop.setPos(pos)
    if hpr:
        prop.setHpr(hpr)
    if scale:
        prop.setScale(scale)

def getPropAppearTrack(prop, parent, posPoints, appearDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, startScale = Point3(0.01), poseExtraArgs = None):
    propTrack = Sequence(
        Wait(appearDelay),
        Func(__showProp, prop, parent, *posPoints)
    )

    if poseExtraArgs:
        propTrack.append(Func(prop.pose, *poseExtraArgs))

    propTrack.append(prop.scaleInterval(scaleUpTime, scaleUpPoint, startScale=startScale))
    return propTrack

def getPropThrowTrack(prop, hitPoints = [], hitDuration = 0.5, lookAt = 'none', parent = None, callback = None):
    if parent is None:
        parent = render

    propTrack = Sequence()
    propTrack.append(Func(prop.wrtReparentTo, parent))

    if lookAt != 'none':
        propTrack.append(Func(prop.lookAt, lookAt))
    
    throwTrack = Sequence()

    for i in range(len(hitPoints)):
        pos = hitPoints[i]
        throwTrack.append(LerpPosInterval(prop, hitDuration, pos=pos))

    if callback is not None:
        throwTrack.append(Func(callback))

    throwTrack.append(Func(removeProp, prop))
    propTrack.append(Func(throwTrack.start))
    return propTrack

def getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs, callback=None):
    particleEffect = partExtraArgs[0]
    parent = partExtraArgs[1]

    if len(partExtraArgs) > 2:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1

    partInterval = ParticleInterval(particleEffect, parent, worldRelative, duration=durationDelay, cleanup=True)
    partTrack = Sequence(Wait(startDelay), Func(partInterval.start))

    if callback is not None:
        partTrack.append(Func(callback))
    
    return partTrack

def getPropTrack(prop, parent, posPoints, appearDelay, remainDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, scaleDownTime = 0.5, startScale = Point3(0.01), anim = 0, propName = 'none', animDuration = 0.0, animStartTime = 0.0):
    if anim == 1:
        return Sequence(
            Wait(appearDelay),
            Func(__showProp, prop, parent, *posPoints),
            LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale=startScale),
            ActorInterval(prop, propName, duration=animDuration, startTime=animStartTime),
            Wait(remainDelay),
            Func(removeProp, prop)
        )
    else:
        return Sequence(
            Wait(appearDelay),
            Func(__showProp, prop, parent, *posPoints),
            LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale=startScale),
            Wait(remainDelay),
            LerpScaleInterval(prop, scaleDownTime, PNT3_NEARZERO),
            Func(removeProp, prop)
        )

def clipOnTie(enemy, hitPoint):
    tie = Actor('phase_3.5/models/props/clip-on-tie-mod.bam', {'clip-on-tie': 'phase_3.5/models/props/clip-on-tie-chan.bam'})
    tie.getChild(0).setHpr(23.86, -16.03, 9.18)

    enemyType = enemy.style.body

    if enemyType == 'a':
        throwDelay = 2.17
    elif enemyType == 'b':
        throwDelay = 2.17
    elif enemyType == 'c':
        throwDelay = 1.45

    enemyTrack = enemy.actorInterval('throw-paper')
    posPoints = [Point3(0.66, 0.51, 0.28), VBase3(-69.652, -17.199, 67.96)]

    propTrack = Sequence(
        getPropAppearTrack(tie, enemy.getRightHand(), posPoints, 0.5, PNT3_ONE, scaleUpTime=0.5, poseExtraArgs=['clip-on-tie', 0]),
        tie.actorInterval('clip-on-tie', duration=throwDelay, startTime=1.1),
        Func(tie.setHpr, 0, -90, 0),
        getPropThrowTrack(tie, [hitPoint], hitDuration=0.4, callback=enemy.arena.damageHQ)
    )

    sound = loader.loadSfx('phase_5/audio/sfx/SA_powertie_throw.ogg')
    soundTrack = Sequence(Wait(throwDelay + 1), SoundInterval(sound, node=enemy))
    return Parallel(enemyTrack, propTrack, soundTrack)

def redTape(enemy, hitPoint):
    tape = loader.loadModel('phase_5/models/props/redtape.bam')

    enemyTrack = enemy.actorInterval('throw-paper')
    enemyName = enemy.getStyleName()

    if enemyName == 'tf' or enemyName == 'nc':
        tapePosPoints = [Point3(-0.24, 0.09, -0.38), VBase3(-1.152, 86.581, -76.784)]
    else:
        tapePosPoints = [Point3(0.24, 0.09, -0.38), VBase3(-1.152, 86.581, -76.784)]

    if enemy.style.body == 'a':
        throwDelay = 1.97
    elif enemy.style.body == 'b':
        throwDelay = 1.97
    elif enemy.style.body == 'c':
        throwDelay = 1.25

    tapeScaleUpPoint = Point3(0.9, 0.9, 0.24)
    propTrack = Sequence(
        getPropAppearTrack(tape, enemy.getRightHand(), tapePosPoints, 0.8, tapeScaleUpPoint, scaleUpTime=0.5),
        Wait(throwDelay),
        getPropThrowTrack(tape, [hitPoint], callback=enemy.arena.damageHQ)
    )

    sound = loader.loadSfx('phase_5/audio/sfx/SA_red_tape.ogg')
    soundTrack = Sequence(Wait(2.9), SoundInterval(sound, node=enemy))
    return Parallel(enemyTrack, propTrack, soundTrack)

def shredder(enemy, hitPoint):
    paper =  Actor('phase_3.5/models/props/shredder-paper-mod.bam', {'shredder-paper': 'phase_3.5/models/props/shredder-paper-chan.bam'})
    shredder = loader.loadModel('phase_3.5/models/props/shredder.bam')
    particleEffect = EffectsManager.createParticleEffect(file='shred')
    enemyTrack = enemy.actorInterval('shredder')

    partTrack = getPartTrack(particleEffect, 3.5, 1.9, [particleEffect, enemy, 0], callback=enemy.arena.damageHQ)
    paperPosPoints = [Point3(0.59, -0.31, 0.81), VBase3(79.224, 32.576, -179.449)]
    paperPropTrack = getPropTrack(paper, enemy.getRightHand(), paperPosPoints, 2.4, 1e-05, scaleUpTime=0.2, anim=1, propName='shredder-paper', animDuration=1.5, animStartTime=2.8)
    shredderPosPoints = [Point3(0, -0.12, -0.34), VBase3(-90.0, -53.77, -0.0)]
    shredderPropTrack = getPropTrack(shredder, enemy.getLeftHand(), shredderPosPoints, 1, 3, scaleUpPoint=Point3(4.81, 4.81, 4.81))

    sound = loader.loadSfx('phase_3.5/audio/sfx/SA_shred.ogg')
    soundTrack = Sequence(Wait(3.4), SoundInterval(sound, node=enemy))
    return Parallel(enemyTrack, paperPropTrack, shredderPropTrack, partTrack, soundTrack)

def rollodex(enemy, hitPoint):
    rollodex = loader.loadModel('phase_5/models/props/roll-o-dex.bam')
    particleEffect2 = EffectsManager.createParticleEffect(file='rollodexWaterfall')
    particleEffect3 = EffectsManager.createParticleEffect(file='rollodexStream')
    enemyType = enemy.style.body

    if enemyType == 'a':
        propPosPoints = [Point3(-0.51, -0.03, -0.1), VBase3(89.673, 2.166, 177.786)]
        propScale = Point3(1.2, 1.2, 1.2)
        part2Delay = 2.8
        part3Delay = 3.2
    elif enemyType == 'b':
        propPosPoints = [Point3(0.12, 0.24, 0.01), VBase3(99.032, 5.973, -179.839)]
        propScale = Point3(0.91, 0.91, 0.91)
        part2Delay = 3.1
        part3Delay = 3.5

    part2Duration = 1.9
    part3Duration = 1
    partTrack2 = getPartTrack(particleEffect2, part2Delay, part2Duration, [particleEffect2, enemy, 0])
    partTrack3 = getPartTrack(particleEffect3, part3Delay, part3Duration, [particleEffect3, enemy, 0], callback=enemy.arena.damageHQ)
    enemyTrack = enemy.actorInterval('roll-o-dex')
    propTrack = getPropTrack(rollodex, enemy.getLeftHand(), propPosPoints, 1e-06, 4.7, scaleUpPoint=propScale, anim=0, propName='rollodex', animDuration=0, animStartTime=0)
    
    sound = loader.loadSfx('phase_5/audio/sfx/SA_rolodex.ogg')
    soundTrack = Sequence(Wait(2.8), SoundInterval(sound, node=enemy))
    return Parallel(enemyTrack, propTrack, soundTrack, partTrack2, partTrack3)

def jargon(enemy, hitPoint):
    particleEffect = EffectsManager.createParticleEffect(file='jargonSpray')
    particleEffect2 = EffectsManager.createParticleEffect(file='jargonSpray')
    particleEffect3 = EffectsManager.createParticleEffect(file='jargonSpray')
    particleEffect4 = EffectsManager.createParticleEffect(file='jargonSpray')
    EffectsManager.setEffectTexture(particleEffect, 'jargon-brow', color=Vec4(1, 0, 0, 1))
    EffectsManager.setEffectTexture(particleEffect2, 'jargon-deep', color=Vec4(0, 0, 0, 1))
    EffectsManager.setEffectTexture(particleEffect3, 'jargon-hoop', color=Vec4(1, 0, 0, 1))
    EffectsManager.setEffectTexture(particleEffect4, 'jargon-ipo', color=Vec4(0, 0, 0, 1))

    partDelay = 1.1
    partInterval = 1.2
    enemyTrack = enemy.actorInterval('speak')
    partTrack = getPartTrack(particleEffect, partDelay + partInterval * 0, 2, [particleEffect, enemy, 0])
    partTrack2 = getPartTrack(particleEffect2, partDelay + partInterval * 1, 2, [particleEffect2, enemy, 0])
    partTrack3 = getPartTrack(particleEffect3, partDelay + partInterval * 2, 2, [particleEffect3, enemy, 0])
    partTrack4 = getPartTrack(particleEffect4, partDelay + partInterval * 3, 1.0, [particleEffect4, enemy, 0], callback=enemy.arena.damageHQ)

    sound = loader.loadSfx('phase_5/audio/sfx/SA_jargon.ogg')
    soundTrack = Sequence(Wait(2.1), SoundInterval(sound, node=enemy))
    return Parallel(enemyTrack, soundTrack, partTrack, partTrack2, partTrack3, partTrack4)

Attacks = {
    'a': [redTape, clipOnTie, rollodex, jargon],
    'b': [redTape, clipOnTie, rollodex, jargon],
    'c': [redTape, clipOnTie, shredder, jargon]
}

def chooseAttack(enemy):
    bodyType = enemy.style.body
    return random.choice(Attacks[bodyType])