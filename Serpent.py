from MovingEntity import MovingEntity
from Exceptions import BoundsError
from CellGrid import CellGrid
from Cell import Cell


class Serpent(MovingEntity):

    def __init__(self, grid):
        super().__init__(grid)

        self.new_direction = 0
        self.body = []
        self.grow_by = 0
        self.grid = grid

        self.real_friction = 70
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

        self.new_direction = direction

    def _move(self):
        self.direction = self.new_direction
        self.set_friction(self.real_friction)

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

        if not self.grid.is_in_bounds(new_x, new_y):
            raise BoundsError

        self.set_position(new_x, new_y)

    def draw(self):
        position = [self.x, self.y]

        # draw the new head
        self.body.insert(0, position)

        cell = Cell(int(self.x), int(self.y), 1, self)
        self.grid.add_cell(cell)

        # erase the tail
        if len(self.body) > 1:
            if not self.grow_by:
                end = self.body.pop()
                self.grid.del_cell_at(int(end[0]), int(end[1]))
            else:
                if self.grow_by:
                    self.grow_by -= 1

    def grow(self,size):
        self.grow_by += size
