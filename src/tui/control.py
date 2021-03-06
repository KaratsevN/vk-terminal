from abc import ABCMeta, abstractmethod

class Control():

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self.height = 0
        self.width = 0
        self.position = [0, 0]
        self.type = ""

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def showProperties(self):
        pass