import curses

class Interface(object):
    def __init__(self):
        self._height = 0
        self._width = 0
        #position x1,y1,x2,y2(rectangle)
        self._position = [0, 0, 0, 0]
        self._style = "ascii"

    def draw(self, position):

        return self._position