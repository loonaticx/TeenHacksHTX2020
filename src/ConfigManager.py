import json
import os


settingsDefault = '''{
    "settings":
    {
        "want-debug-mode": false,
        "want-logging": false,
    }
}
'''


class ConfigManager:
    def __init__(self):
        pass
        #self.generateSettings()

    def generateSettings(self):
        if not os.path.exists('config/'):
            os.mkdir('config/')

        if not os.path.isfile('config/settings.json'):
            with open('config/settings.json', 'w') as data:
                data.write(settingsDefault)
                data.close()

    def loadSettings(self):
        with open('config/settings.json') as data:
            return json.load(data)

#print(settings["settings"][0]['want-gay-ass-filters'])
#rint (settings["settings"][0]['want-ambient-occlusion'])
#print (settings["settings"][1]['value'])

#print(settings["settings"])



#generateColors()




