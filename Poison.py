from random import randint
from Entity import Entity


class Poison(Entity):
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.set_position(
            randint(0, window.width-1),
            randint(0, window.height-1)
        )

    def draw(self):
        self.window.put_char(int(self.x), int(self.y), ' ', 3)

    def erase(self):
        self.window.put_char(int(self.x), int(self.y), ' ', 4)
