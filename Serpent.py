import curses
from MovingEntity import MovingEntity


class Serpent(MovingEntity):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    x = 0
    y = 0
    direction = 0
    length = 2
    body = []

    def __init__(self, window):
        super().__init__()
        self.window = window

    def set_direction(self, direction):
        self.direction = direction

        if self.direction == self.LEFT or self.direction == self.RIGHT:
            self.set_friction(20)

        elif self.direction == self.UP or self.direction == self.DOWN:
            self.set_friction(30)

    def _move(self):

        new_x = self.x
        new_y = self.y

        if self.direction == self.LEFT:
            new_x = self.x - 1

        elif self.direction == self.RIGHT:
            new_x = self.x + 1

        elif self.direction == self.UP:
            new_y = self.y - 1

        elif self.direction == self.DOWN:
            new_y = self.y + 1

        if not self.window.in_bounds(new_x, new_y):
            return

        self.set_position(new_x, new_y)

        position = [0,0]
        position[0] = self.x
        position[1] = self.y

        if len(self.body):
            end = self.body.pop()
            self.window.addch(int(end[1]), int(end[0]), ' ')

        self.body.insert(0, position)
        self.window.addch(int(self.body[0][1]), int(self.body[0][0]), curses.ACS_CKBOARD)

    def update_body(self, length):
        self.length = length

