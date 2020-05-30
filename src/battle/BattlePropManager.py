from direct.actor import Actor


class BattlePropManager():
    def getProp(self, name):
        return self.__getPropCopy(name)

    def __getPropCopy(self, name):
        if self.propTypes[name] == 'actor':
            if name not in self.props:
                prop = Actor.Actor()
                prop.loadModel(self.propStrings[name][0])
                animDict = {}
                animDict[name] = self.propStrings[name][1]
                prop.loadAnims(animDict)
                prop.setName(name)
                self.storeProp(name, prop)
                #if name in Variants:
                    #self.makeVariant(name)
            return Actor.Actor(other=self.props[name])
        else:
            if name not in self.props:
                prop = loader.loadModel(self.propStrings[name][0])
                prop.setName(name)
                self.storeProp(name, prop)
                #if name in Variants:
                    #self.makeVariant(name)
            return self.props[name].copyTo(hidden)

BattlePropMan = BattlePropManager()