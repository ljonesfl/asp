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
        self.body = []
        self.grow_by = 0

        self.window = window
        self.real_friction = 30
        self.set_friction(self.real_friction)

    def get_friction(self):
        return self.real_friction

    def set_friction(self, friction):

        if friction < 10:
            friction = 10

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

    def draw(self):
        position = [self.x, self.y]

        # draw the new head
        self.body.insert(0, position)
        self.window.addch(int(self.y), int(self.x), curses.ACS_CKBOARD)

        # erase the tail
        if len(self.body) > 1:
            if not self.grow_by:
                end = self.body.pop()
                self.window.addch(int(end[1]), int(end[0]), ' ')
            else:
                self.grow_by -= 1

        super().draw()

    def grow(self,size):
        self.grow_by += size

    def collision(self, entity):
        collided = False

        start = 0
        end = len(self.body)

        # if checking for a self collision, don't look for the head position.

        if entity == self:
            start = 1

        for x in range(start, end):
            cell = self.body[x]

            if cell[0] == entity.x and cell[1] == entity.y:
                collided = True

        return collided

