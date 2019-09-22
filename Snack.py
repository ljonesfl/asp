from random import randint
from Entity import Entity
import curses


class Snack(Entity):
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.set_position(
            randint(0, window.width-1),
            randint(0, window.height-1)
        )

    def draw(self):
        self.window.addch(int(self.y), int(self.x), curses.ACS_CKBOARD)

    def erase(self):
        self.window.addch(int(self.y), int(self.x), ' ')
