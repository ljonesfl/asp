from Exceptions import Collision
from Exceptions import GameOver
from Exceptions import BoundsError
from Exceptions import LevelCompleted
from Exceptions import Error

from Snack import Snack
from Poison import Poison
from Serpent import Serpent
from random import randint
from MovingEntity import MovingEntity
from CellGrid import CellGrid


class Arena:

    def __init__(self, window, width, height):

        self.grid = CellGrid(window, width, height)
        self.moving_entities = []
        self.player1 = None
        self.score = 0
        self.snack_count = 0
        self.level = None
        self.window = window

    def set_level(self, level):
        self.level = level

        self.moving_entities = []
        self.grid.reset()
        self.snack_count = 0

        for x in range(0, level.entities):
            entity = self.entity_factory()

            try:
                entity.draw()
            except Collision:
                pass

        snake = Serpent(self.grid)

        snake.set_position(
            randint(0, self.grid.width),
            randint(0, self.grid.height)
        )

        snake.grow(self.level.initial_snake_length)

        self.set_player1(snake)
        self.add_moving(snake)

    def set_player1(self, player1):
        self.player1 = player1

        if self.player1.x < 20:
            self.player1.set_direction(MovingEntity.LEFT)

        if self.player1.x > self.window.width - 20:
            self.player1.set_direction(MovingEntity.RIGHT)

        if self.player1.y < 20:
            self.player1.set_direction(MovingEntity.DOWN)

        if self.player1.y > self.window.height - 20:
            self.player1.set_direction(MovingEntity.UP)

    def add_static(self, static_entity):
        try:
            self.grid.add_cell(static_entity)
            if isinstance(static_entity, Snack):
                self.snack_count += 1
        except Collision:
            pass
        except KeyError:
            self.grid.del_entity(static_entity)
            self.grid.add_entity(static_entity)
            if isinstance(static_entity, Snack):
                self.snack_count += 1

    def add_moving(self, moving_entity):
        self.moving_entities.append(moving_entity)

    def snake_eats_snack(self, snack, snake):
        # snack.erase()
        # self.del_static(snack)
        self.score += 1
        self.snack_count -= 1

        snake.grow(self.level.snack_growth_factor)
        snake.set_friction(snake.get_friction() - self.level.snake_friction_factor)

        if self.get_snack_count() == 0:
            raise LevelCompleted

    def snake_eats_poison(self, poison, snake):
        raise GameOver("You ate the poison!!!")

    def snake_eats_self(self,snake):
        raise GameOver("You bit yourself!!!")

    def get_snack_count(self):
        return self.snack_count

    def test_all_moving(self):
        # Test all moving entities against static and moving
        for entity in self.moving_entities:
            self.test_moving(entity)
            self.test_static(entity)

    def test_moving(self, entity):
        for entity_test in self.moving_entities:
            if entity.collision(entity_test):
                raise Collision(entity, entity_test)

    def test_static(self, entity):
        try:
            cell = self.grid.get_cell_at(entity.x, entity.y)
            if cell:
                raise Collision(entity, cell.parent)
        except KeyError:
            pass

    def entity_factory(self):
        entity_type = randint(0, self.level.poison_ratio - 1)

        if entity_type == 0:
            entity = Poison(self.grid)
        else:
            entity = Snack(self.grid)
            self.snack_count += 1

        return entity

    def tick(self):

        try:
            for entity in self.moving_entities:
                entity.move()

        except BoundsError:
            raise GameOver("You went off the end of the world!!!")

        except Collision as c:
            player1 = None
            entity = None

            if c.entity1 is self.player1 or c.entity2 is self.player1:
                if c.entity1 is self.player1:
                    player1 = c.entity1
                    entity = c.entity2
                else:
                    player1 = c.entity2
                    entity = c.entity1

            if player1:
                if isinstance(entity, Snack):
                    self.snake_eats_snack(entity, player1)

                if isinstance(entity, Poison):
                    self.snake_eats_poison(entity, player1)

                if isinstance(entity, Serpent):
                    self.snake_eats_self(player1)

