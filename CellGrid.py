"""
CellGrid is a 2d representation of the screen.
The grid is a collection of Cell objects. Anything drawn on the screen will be represented by a location in the grid.
A collision will take place any time an attempt is made to draw a cell upon an existing cell.
"""

from Cell import Cell
from Exceptions import Collision
from Exceptions import BoundsError


class CellGrid(object):

    def __init__(self, window, width, height):
        self.width = width
        self.height = height
        self.window = window
        self.__grid = None

        self.reset()

    def reset(self):
        self.__grid = [[None for y in range(self.height)] for x in range(self.width)]

    def del_cell_at(self, x, y):
        self.__grid[x][y] = None
        if self.window:
            self.window.put_char(int(x), int(y), ' ', 4)

    def del_cell(self, cell):
        self.del_cell_at(cell.x, cell.y)

    def add_cell(self, cell):
        if not self.is_in_bounds(cell.x, cell.y):
            return False

        current = self.get_cell_at(cell.x, cell.y)

        self.__grid[cell.x][cell.y] = cell

        if self.window:
            self.window.put_char(int(cell.x), int(cell.y), ' ', cell.color)

        if current is not None:
            raise Collision(cell.parent, current.parent)

        return True

    def is_in_bounds(self, x, y):
        if x >= self.width:
            raise BoundsError

        if y >= self.height:
            raise BoundsError

        if x < 0:
            raise BoundsError

        if y < 0:
            raise BoundsError


        return True

    def get_cell_at(self, x, y):

        if not self.is_in_bounds(x, y):
            return False

        cell = self.__grid[x][y]

        return cell


