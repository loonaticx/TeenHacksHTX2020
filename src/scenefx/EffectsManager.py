import math
from panda3d.core import Fog, LVecBase4
from direct.particles.ParticleEffect import *
from . import ParticleDefs

# EffectsManager.fog.loadFog(arg)?
particleModel = None

def getParticleModel():
    global particleModel

    if particleModel is None:
        particleModel = loader.loadModel('phase_3.5/models/props/suit-particles')
    
    return particleModel

def getParticle(name):
    return getParticleModel().find('**/{0}'.format(name))

def loadParticleFile(name):
    setupParticle = ParticleDefs.ParticleTable[name]
    effect = ParticleEffect()

    setupParticle(effect)
    return effect

def __makeGearExplosion(numParticles = None, style = 'Normal'):
    if style == 'Normal':
        effect = loadParticleFile('gearExplosion')
    elif style == 'Big':
        effect = loadParticleFile('gearExplosionBig')
    elif style == 'Wide':
        effect = loadParticleFile('gearExplosionWide')

    if numParticles:
        particles = effect.getParticlesNamed('particles-1')
        particles.setPoolSize(numParticles)

    return effect

def createParticleEffect(name = None, file = None, numParticles = None):
    if not name:
        return loadParticleFile(file)
    if name == 'GearExplosion':
        return __makeGearExplosion(numParticles)
    elif name == 'BigGearExplosion':
        return __makeGearExplosion(numParticles, 'Big')
    elif name == 'WideGearExplosion':
        return __makeGearExplosion(numParticles, 'Wide')

def setEffectTexture(effect, name, color = None):
    particles = effect.getParticlesNamed('particles-1')
    np = getParticle(name)

    if color:
        particles.renderer.setColor(color)

    particles.renderer.setFromNode(np)

def loadShaders():
    normalsBuffer = base.win.makeTextureBuffer("normalsBuffer", 0, 0)
    normalsBuffer.setClearColor(LVecBase4(0.5, 0.5, 0.5, 1))
    normalsBuffer = normalsBuffer
    normalsCamera = base.makeCamera(
        normalsBuffer, lens=base.cam.node().getLens())
    normalsCamera.node().setScene(render)

    drawnScene = normalsBuffer.getTextureCard()
    drawnScene.setTransparency(1)
    drawnScene.setColor(1, 1, 1, 0)
    drawnScene.reparentTo(render2d)
    print("loading shaders...")
    return drawnScene

def toggleAmbientOcclusion(AOEnabled):
    if not AOEnabled:
        filters.setAmbientOcclusion()
        return True
    else:
        filters.delAmbientOcclusion()
        return False

def toggleInvert():
    if not invertEnabled:
        filters.setInverted()
        invertEnabled = True
    else:
        filters.delInverted()
        invertEnabled = False

def toggleBloom():
    if not bloomEnabled:
        filters.setBloom()
        bloomEnabled = True
    else:
        filters.delBloom()
        bloomEnabled = False

def toggleCamera():
    if not mouseEnabled:
        base.enableMouse()
        mouseEnabled = True
    else:
        base.disableMouse()
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        mouseEnabled = False

def toggleFog(fog, fogEnabled, FogDensity):
    if not fogEnabled:
        return fog.setExpDensity(FogDensity)
        #return True
    else:
        return fog.setExpDensity(0)
        #return False

def toggle_xray_mode():
    """Toggle X-ray mode on and off. This is useful for seeing the
    effectiveness of the portal culling."""
    xray_mode = not xray_mode
    if xray_mode:
        scene.setColorScale((1, 1, 1, 0.5))
        scene.setTransparency(TransparencyAttrib.MDual)
    else:
        scene.setColorScaleOff()
        scene.setTransparency(TransparencyAttrib.MNone)

def toggle_model_bounds():
    """Toggle bounding volumes on and off on the models."""
    show_model_bounds = not show_model_bounds
    if show_model_bounds:
        for model in objectList:
            model.showBounds()
    else:
        for model in objectList:
            model.hideBounds()
