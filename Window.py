import _curses
from Exceptions import BoundsError


class Window(object):

    def __init__(self, curses_window, width, height):
        self.window = curses_window
        self.window.nodelay(1)
        self.width = width
        self.height = height
        self.window.timeout(1)

    def in_bounds(self, x, y):
        if x < 0 or x >= self.width:
            return False

        if y < 0 or y >= self.height:
            return False

        return True

    def addch(self, y, x, char):

        if not self.in_bounds(x, y):
            raise BoundsError

        try:
            self.window.addch(y, x, char)
        except _curses.error as e:
            pass
