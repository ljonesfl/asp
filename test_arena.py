import unittest
from Arena import Arena
from Entity import Entity
from Exceptions import Collision

class ArenaTest(unittest.TestCase):
    def test_collision_pass(self):
        arena = Arena(None, 10, 10)

        with self.assertRaises(Collision):
            entity1 = Entity(arena.grid)
            entity1.x = 1
            entity1.y = 1

            entity1.draw()

            entity2 = Entity(arena.grid)
            entity2.x = 1
            entity2.y = 1

            entity2.draw()

    def test_collision_fail(self):
        arena = Arena(None, 10, 10)

        entity1 = Entity(arena.grid)
        entity1.x = 1
        entity1.y = 1

        entity2 = Entity(arena.grid)
        entity2.x = 1
        entity2.y = 2

        arena.add_static(entity1)
        arena.add_static(entity2)

        arena.process_collisions()

