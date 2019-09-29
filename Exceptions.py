
class Error(Exception):
    pass


class BoundsError(Error):
    pass


class Collision(Error):
    def __init__(self, entity1, entity2):
        self.entity1 = entity1
        self.entity2 = entity2


class GameOver(Error):
    pass