
class Entity(object):

    def __init__(self):
        self.x = 0
        self.y = 0

    def set_position(self, x, y):
        if x < 0:
            x = 0

        if y < 0:
            y = 0

        self.x = x
        self.y = y

    def collision(self, entity):
        collided = False

        if self.x == entity.x and self.y == entity.y:
            collided = True

        return collided

    def draw(self):
        pass

    def erase(self):
        pass