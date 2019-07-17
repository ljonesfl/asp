from Entity import Entity


class MovingEntity(Entity):

    def __init__(self):
        self.__friction = 0
        self.__ticks = 0

    def should_move(self):
        self.__ticks = self.__ticks + 1
        if self.__ticks >= self.__friction:
            return True

        return False

    def set_friction(self, friction):
        self.__friction = friction

    def set_position(self, x, y):
        super().set_position(x, y)
        self.__ticks = 0

