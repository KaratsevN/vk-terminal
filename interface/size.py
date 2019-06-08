import os
import console
import curses
#I don't know why I'll add curses.panel


class Size():
    def __init__(self):
        self._rows = 0
        self._columns = 0
        #size = os.get_terminal_size()
        #_columns = size.columns
        #_rows = size.lines
        #self._rows, self._columns = os.popen('stty size', 'r').read().split()

    def getSize(self):
        try:
            (self._rows, self._columns) = console.getTerminalSize()
            #self._rows, self._columns = os.popen('stty size', 'r').read().split()
            return self._rows , self._columns
        except Exception:
            print('Ваша консоль не поддерживает getSize, поэтому работаем в штатном режиме:', end='\n')
        else:
            print('Lol wtf?!')

    def printSize(self):
        print(self._rows, self._columns)