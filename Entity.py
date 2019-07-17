

class Entity(object):
    x = 0
    y = 0

    def set_position(self, x, y):
        if x < 0:
            x = 0

        if y < 0:
            y = 0

        self.x = x
        self.y = y

