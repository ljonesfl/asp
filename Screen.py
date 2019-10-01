import curses
from Window import Window


class Screen:

    def __init__(self):
        screen = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        self.screen = screen

        curses.init_pair(1, -1, curses.COLOR_BLUE)

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)

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

#    def clear(self):
#        self.screen.clear()
#        self.screen.refresh()
