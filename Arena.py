from Exceptions import Collision
from Snack import Snack
from Serpent import Serpent


class Arena:

    def __init__(self):
        self.moving_entities = []
        self.static_entities = {}
        self.player1 = None
        self.score = 0
        self.snack_count = 0

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

                if isinstance(entity, Serpent):
                    self.snake_eats_self(player1)

    def snake_eats_snack(self, snack, snake):
        # snack.erase()
        self.del_static(snack)
        self.score += 1

        snake.grow(5)
        snake.set_friction(snake.get_friction() - 2)

        if self.get_snack_count() == 0:
            print('score ' + str(self.score))
            exit()

    def snake_eats_self(self,snake):
        print('OUCH! score ' + str(self.score))
        exit()

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
