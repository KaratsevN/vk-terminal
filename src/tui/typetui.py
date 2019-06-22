from settings.settings import settings

class TypeTui():

    def __init__(self):
        if(settings['type']):
            self.type = settings['type']
            return self.type
        else:
            self.type = 'ascii'
            return self.type

    def getType(self):
        return self.type

    def setType(self, type):
        self.type, settings['type'] = type
        return True