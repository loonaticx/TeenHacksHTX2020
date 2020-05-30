from panda3d.core import VBase4
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *

CreampieColor = VBase4(250.0 / 255.0, 241.0 / 255.0, 24.0 / 255.0, 1.0)
FruitpieColor = VBase4(55.0 / 255.0, 40.0 / 255.0, 148.0 / 255.0, 1.0)
BirthdayCakeColor = VBase4(253.0 / 255.0, 119.0 / 255.0, 220.0 / 255.0, 1.0)
RegularColor = VBase4(1.0, 1.0, 1.0, 1.0)
Splats = {
 'tart': (0.3, FruitpieColor),
 'fruitpie-slice': (0.5, FruitpieColor),
 'creampie-slice': (0.5, CreampieColor),
 'fruitpie': (0.7, FruitpieColor),
 'creampie': (0.7, CreampieColor),
 'birthday-cake': (0.9, BirthdayCakeColor),
 'wedding-cake': (0.9, BirthdayCakeColor)
}

def getPieSplatInterval(pos, pieName):
    scale, color = Splats[pieName]
    splat = Actor('phase_3.5/models/props/splat-mod', {'splat': 'phase_3.5/models/props/splat-chan'})
    splat.setBillboardPointWorld(2)
    splat.setScale(scale)
    splat.setColor(color)
    sound = loader.loadSfx('phase_4/audio/sfx/AA_wholepie_only.ogg')

    return Parallel(
        Func(splat.reparentTo, render),
        Func(splat.setPos, pos),
        SoundInterval(sound, node=splat, volume=1.0),
        Sequence(
            ActorInterval(splat, 'splat'),
            Func(splat.detachNode)
        )
    )