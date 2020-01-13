import unittest
from Entity import Entity
from CellGrid import CellGrid
from Cell import Cell
from Exceptions import BoundsError


class MyTestCase(unittest.TestCase):

    def test_grid_bounds_pass(self):
        grid = CellGrid(None, 100, 50)

        entity = Entity(grid)
        entity.x = 99
        entity.y = 49

        cell = Cell(entity.x, entity.y, 1, entity)

        self.assertTrue(grid.add_cell(cell))

    def test_grid_bounds_fail(self):
        grid = CellGrid(None, 100, 50)

        entity = Entity(grid)
        entity.x = 101
        entity.y = 51

        with self.assertRaises(BoundsError):
            cell = Cell(entity.x, entity.y, 1, entity)
            grid.add_cell(cell)

    def test_get_entity(self):
        grid = CellGrid(None,100, 50)

        entity = Entity(grid)
        entity.x = 99
        entity.y = 49

        cell = Cell(entity.x, entity.y, 1, entity)

        grid.add_cell(cell)

        self.assertTrue(grid.get_cell_at(entity.x, entity.y))


if __name__ == '__main__':
    unittest.main()
