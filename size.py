import os


class Size():
    _rows = 0
    _columns = 0

    def __init__(self):
        _columns = 0
        _rows = 0
        # _rows, _columns = os.popen('stty size', 'r').read().split()

    def isSizeWork(self):
        try:
            os.get_terminal_size()
            return True
        except:
            from locales.ru.messages import data
            print(data['error_size']['message'])
            return False

    def getSize(self):
        if self.isSizeWork():
            _columns = os.get_terminal_size().columns
            _rows = os.get_terminal_size().lines
            return self._rows, self._columns