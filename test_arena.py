import unittest
from Arena import Arena
from Entity import Entity
from Exceptions import Collision


class ArenaTest(unittest.TestCase):
    def test_collision_pass(self):
        arena = Arena()

        entity1 = Entity()
        entity1.x = 1
        entity1.y = 1

        entity2 = Entity()
        entity2.x = 1
        entity2.y = 1

        arena.add_static(entity1)
        arena.add_static(entity2)

        with self.assertRaises(Collision):
            arena.process_collisions()

    def test_collision_fail(self):
        arena = Arena()

        entity1 = Entity()
        entity1.x = 1
        entity1.y = 1

        entity2 = Entity()
        entity2.x = 1
        entity2.y = 2

        arena.add_static(entity1)
        arena.add_static(entity2)

        arena.process_collisions()

