
class Arena:

    def __init__(self):
        self.moving_entities = []
        self.static_entities = []

    def add_static(self, static_entity):
        self.static_entities.append(static_entity)

    def add_moving(self, moving_entity):
        self.moving_entities.append(moving_entity)

    