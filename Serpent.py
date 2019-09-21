import curses
from MovingEntity import MovingEntity


class Serpent(MovingEntity):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    def __init__(self, window):
        super().__init__()

        self.x = 0
        self.y = 0
        self.direction = 0
        self.length = 2
        self.body = []

        self.window = window
        self.real_friction = 50
        self.set_friction(self.real_friction)

    def get_friction(self):
        return self.real_friction

    def set_friction(self, friction):
        self.real_friction = friction

        if self.direction == self.UP or self.direction == self.DOWN:
            super().set_friction(self.real_friction * 2)
        else:
            super().set_friction(friction)

    def set_direction(self, direction):

        if self.direction == self.LEFT and direction == self.RIGHT:
            return

        if self.direction == self.RIGHT and direction == self.LEFT:
            return

        if self.direction == self.UP and direction == self.DOWN:
            return

        if self.direction == self.DOWN and direction == self.UP:
            return

        self.direction = direction
        self.set_friction(self.real_friction)

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

    def grow(self):
        self.length += 1
        position = [0,0]
        position[0] = self.x
        position[1] = self.y

        self.body.append(position)
