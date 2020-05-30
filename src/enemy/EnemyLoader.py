from direct.directnotify.DirectNotifyGlobal import directNotify
from . import EnemyDNA
from .EnemyDict import EnemyParts, ModelDict

notify = directNotify.newCategory('EnemyLoader')
notify.setInfo(True)

Preloaded = {}
EnemyDialogArray = []
SkelEnemyDialogArray = []

def loadModels():
    global Preloaded
    if not Preloaded:
        print('Preloading enemies...')
        for filepath in EnemyParts:
            Preloaded[filepath] = loader.loadModel(filepath + '.bam')
            Preloaded[filepath].flattenMedium()

def loadEnemyModelsAndAnims():
    for key in ModelDict.keys():
        model, phase = ModelDict[key]
        filepath = 'phase_3.5' + model + 'mod'
        Preloaded[filepath] = loader.loadModel(filepath)
        filepath = 'phase_' + str(phase) + model + 'heads'
        Preloaded[filepath] = loader.loadModel(filepath + '.bam')

def loadDialog():
    global EnemyDialogArray
    if len(EnemyDialogArray) > 0:
        return
    else:
        loadPath = 'phase_3.5/audio/dial/'
        EnemyDialogFiles = ['COG_VO_grunt',
         'COG_VO_murmur',
         'COG_VO_statement',
         'COG_VO_question',
         'COG_VO_exclaim']
        for file in EnemyDialogFiles:
            EnemyDialogArray.append(base.loadSfx(loadPath + file + '.ogg'))

        EnemyDialogArray.append(EnemyDialogArray[2])


def loadSkelDialog():
    global SkelEnemyDialogArray
    if len(SkelEnemyDialogArray) > 0:
        return
    else:
        grunt = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_grunt.ogg')
        murmur = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_murmur.ogg')
        statement = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_statement.ogg')
        question = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_question.ogg')
        exclaim = loader.loadSfx('phase_5/audio/sfx/Skel_COG_VO_exclaim.ogg')
        SkelEnemyDialogArray = [grunt,
         murmur,
         statement,
         question,
         exclaim,
         statement]