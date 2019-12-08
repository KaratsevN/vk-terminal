from src.tui.control import Control
from src.size import ConsoleSize
import curses
import curses.panel
from src.tui.graphic_elements.dos_style import graphics

# I don't know why I'll add curses.panel


class TextBox(Control):

    def __init__(self, width, height, position, type='ascii'):
        self.stdscr = curses.initscr()
        self.stdscr.keypad(True)
        self.height = height
        self.width = width
        self.position = position
        self.type = type
        self.area = self.height*self.width
        # This is very important thing in boxes. This indicates the cursor position
        self.anchor = [position[0]+1,position[1]+1];

    def draw(self, size):
        #if (width > 0) or (height > 0):
        # drawing top corners
        # maxy, maxx = self.win.getmaxyx()
        self.stdscr.addstr(self.position[1], self.position[0], graphics["left-up"])
        self.stdscr.addstr(self.position[1], self.position[0] + self.width - 1, graphics["right-up"])

        # drawing bottom corners
        self.stdscr.addstr(self.position[1] + self.height, self.position[0], graphics["left-down"])
        self.stdscr.addstr(self.position[1] + self.height, self.position[0] + self.width - 1, graphics["right-down"])

        # drawing horizontal border
        for i in range(1, self.width - 1):
            self.stdscr.addstr(self.position[1], self.position[0] + i, graphics["horizontal-border"])
            self.stdscr.addstr(self.position[1] + self.height, self.position[0] + i, graphics["horizontal-border"])

        # drawing vertical border
        for i in range(1, self.height):
            self.stdscr.addstr(self.position[1] + i, self.position[0], graphics["vertical-border"])
            self.stdscr.addstr(self.position[1] + i, self.position[0] + self.width - 1, graphics["vertical-border"])

        self.stdscr.addstr(self.anchor[1], self.anchor[0], str(size[0]))
        self.stdscr.addstr(size[1] - 1, size[0] - 2, "R")
        #self.stdscr.addstr(self.position[0] + 1, self.position[1] + 1, "abcdefgh")

    def update(self):
        pass

    def showProperties(self):
        pass
