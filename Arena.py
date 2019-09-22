from Exceptions import Collision
from Snack import Snack
from Serpent import Serpent

class Arena:

    def __init__(self):
        self.moving_entities = []
        self.static_entities = []
        self.player1 = None
        self.score = 0

    def set_player1(self, player1):
        self.player1 = player1

    def add_static(self, static_entity):
        self.static_entities.append(static_entity)

    def add_moving(self, moving_entity):
        self.moving_entities.append(moving_entity)

    def del_static(self, static_entity):
        index = self.static_entities.index(static_entity)
        del self.static_entities[index]

    def process_collisions(self):
        try:
            if self.player1.collision(self.player1):
                raise Collision(self.player1, self.player1)

            self.test_all_moving()
            self.test_all_static()
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

                if isinstance(entity, Serpent):
                    self.snake_eats_self(player1)

    def snake_eats_snack(self, snack, snake):
        # snack.erase()
        self.del_static(snack)
        self.score += 1

        snake.grow(20)
        snake.set_friction(snake.get_friction() - 5)

        if self.get_snack_count() == 0:
            print('score ' + str(self.score))
            exit()

    def snake_eats_self(self,snake):
        print('OUCH! score ' + str(self.score))
        exit()

    def get_snack_count(self):
        count = 0
        for entity in self.static_entities:
            if isinstance(entity, Snack):
                count += 1

        return count

    def test_all_moving(self):
        # Test all moving entities against static and moving
        for entity in self.moving_entities:
            self.test_static(entity)
            self.test_moving(entity)

    def test_all_static(self):
        # Test all static entities against static and moving
        for entity in self.static_entities:
            self.test_static(entity)
            self.test_moving(entity)

    def test_moving(self, entity):
        for entity_test in self.moving_entities:
            if entity is entity_test:
                continue

            if entity.collision(entity_test):
                raise Collision(entity, entity_test)

    def test_static(self, entity):
        for entity_test in self.static_entities:
            if entity is entity_test:
                continue

            if entity.collision(entity_test):
                raise Collision(entity, entity_test)
