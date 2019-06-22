from src.tui.control import Control
from src.size import ConsoleSize
import curses
import curses.panel


# I don't know why I'll add curses.panel


class TextBox(Control):

    def __init__(self, width, height, position, type='ascii'):
        self.stdscr = curses.initscr()
        self.stdscr.keypad(True)
        self.height = height
        self.width = width
        self.position = position
        self.type = type

    def draw(self, size):
        for i in range(0, self.width):
            self.stdscr.addstr(self.position[0], self.position[1] + i, "-")
            self.stdscr.addstr(self.position[0] + self.height, self.position[1] + i, "-")
        for i in range(1, self.height):
            self.stdscr.addstr(self.position[0] + i, self.position[1], "|")
            self.stdscr.addstr(self.position[0] + i, self.position[1] + self.width - 1, "|")
        # for

    def update(self):
        pass

    def showProperties(self):
        pass
