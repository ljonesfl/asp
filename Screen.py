import curses
from Window import Window


class Screen:

    def __init__(self):
        screen = curses.initscr()
        self.screen = screen

        curses.noecho()

        curses.curs_set(0)

    def __del__(self):
        curses.echo()
        curses.curs_set(1)

    def create_window(self, width=0, height=0):
        max_y, max_x = self.screen.getmaxyx()

        if width == 0:
            width = max_x

        if height == 0:
            height = max_y

        window = Window(curses.newwin(height, width, 0, 0), width, height)

        return window

