from Entity import Entity


class MovingEntity(Entity):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    def __init__(self):
        super().__init__()

        self.__friction = 0
        self.__ticks = 0
        self.direction = 0
        self.__is_moving = True

    def set_is_moving(self, moving):
        self.__is_moving = moving

    def get_is_moving(self):
        return self.__is_moving

    def should_move(self):
        if not self.get_is_moving():
            return False

        self.__ticks += 1
        if self.__ticks >= self.__friction:
            return True

        return False

    def set_friction(self, friction):
        self.__friction = friction

    def get_friction(self):
        return self.__friction

    def set_position(self, x, y):
        super().set_position(x, y)
        self.__ticks = 0

    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        if not self.should_move():
            return

        self._move()
        self.draw()

    def _move(self):
        pass

