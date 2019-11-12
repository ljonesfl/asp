from random import randint
from Entity import Entity
from Cell import Cell


class Poison(Entity):
    def __init__(self, grid):
        super().__init__(grid)

        self.set_position(
            randint(0, grid.width-1),
            randint(0, grid.height-1)
        )

    def draw(self):
        cell = Cell(self.x, self.y, 3, self)
        self.grid.add_cell(cell)
