import os
from tui.control import Control


class ConsoleSize(Control):

    def __init__(self):

        # _rows, _columns = os.popen('stty size', 'r').read().split()

    def isSizeWork(self):
        try:
            os.get_terminal_size()
            return True
        except:
            from locales.ru.messages import data
            #print(data['error_size']['message'])
            return False

    def getSize(self):
        if self.isSizeWork():
            _columns = os.get_terminal_size().columns
            _rows = os.get_terminal_size().lines
            return self._rows, self._columns
        else:
            return None
