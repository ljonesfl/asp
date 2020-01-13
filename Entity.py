"""
An entity is an object that contains a position.
"""

from CellGrid import CellGrid
from Cell import Cell


class Entity(object):

    def __init__(self, grid):
        self.x = 0
        self.y = 0
        self.grid = grid

    def set_position(self, x, y):
        if x < 0:
            x = 0

        if y < 0:
            y = 0

        self.x = x
        self.y = y

    def collision(self, entity):
        collided = False

        if self.x == entity.x and self.y == entity.y:
            collided = True

        return collided

    def draw(self):
        cell = Cell(self.x, self.y, 2, self)
        self.grid.add_cell(cell)

    def erase(self):
        self.grid.del_cell_at(int(self.x), int(self.y))
