from Exceptions import Collision
from Exceptions import GameOver
from Snack import Snack
from Poison import Poison
from Serpent import Serpent
from random import randint


class Arena:

    def __init__(self, window):
        self.moving_entities = []
        self.static_entities = {}
        self.player1 = None
        self.score = 0
        self.snack_count = 0
        self.level = None
        self.window = window

    def set_level(self, level):
        self.level = level

        for x in range(0, level.snacks):
            entity = self.entity_factory()
            entity.draw()
            self.add_static(entity)

        snake = Serpent(self.window)

        snake.set_direction(randint(0, 3))

        snake.set_position(
            randint(0, self.window.width),
            randint(0, self.window.height)
        )

        snake.grow(self.level.initial_length)

        self.set_player1(snake)
        self.add_moving(snake)

    def set_player1(self, player1):
        self.player1 = player1

    def add_static(self, static_entity):
        try:
            self.static_entities[static_entity.x].append(static_entity)
        except KeyError:
            self.static_entities[static_entity.x] = [];
            self.static_entities[static_entity.x].append(static_entity)

        if isinstance(static_entity, Snack):
            self.snack_count += 1

    def add_moving(self, moving_entity):
        self.moving_entities.append(moving_entity)

    def del_static(self, static_entity):
        statics = self.static_entities[static_entity.x]
        index = statics.index(static_entity)
        del statics[index]

        if isinstance(static_entity, Snack):
            self.snack_count -= 1

    def process_collisions(self):
        try:
            self.test_all_moving()
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

    def snake_eats_snack(self, snack, snake):
        # snack.erase()
        self.del_static(snack)
        self.score += 1

        snake.grow(self.level.snack_factor)
        snake.set_friction(snake.get_friction() - self.level.friction_factor)

        if self.get_snack_count() == 0:
            raise GameOver

    def snake_eats_poison(self, poison, snake):
        raise GameOver

    def snake_eats_self(self,snake):
        raise GameOver

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
            statics = self.static_entities[entity.x]
            for entity_test in statics:
                if entity.collision(entity_test):
                    raise Collision(entity, entity_test)
        except KeyError:
            pass

    def entity_factory(self):
        type = randint(0, 9)

        entity = None

        if type % 2:
            entity = Snack(self.window)
        else:
            entity = Poison(self.window)

        return entity

    def tick(self):

        for entity in self.moving_entities:
            entity.move()

        self.process_collisions()

