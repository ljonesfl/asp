import curses
import time
from random import randint

from Keyboard import Keyboard
from Serpent import Serpent
from Arena import Arena
from Snack import Snack
from Exceptions import Collision

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.arena = Arena()

    def play(self):
        ticks = 0
        window = self.screen.create_window()
        keyboard = Keyboard(window)

        snake = Serpent(window)

        snake.set_direction(randint(0, 3))

        snake.set_position(
            randint(0, window.width),
            randint(0, window.height)
        )

        self.arena.set_player1(snake)
        self.arena.add_moving(snake)

        for x in range(0, 1000):
            snack = Snack(window)
            snack.draw()
            self.arena.add_static(snack)

        paused = False

        while True:
            ticks = ticks + 1

            ch = keyboard.get()

            if paused:
                if ch > 0:
                    paused = False
                else:
                    time.sleep(.25)
                    continue
            else:
                if ch == 112:
                    paused = True

            if ch == 113:
                exit()

            if ch == curses.KEY_RIGHT:
                snake.set_direction(snake.RIGHT)

            if ch == curses.KEY_LEFT:
                snake.set_direction(snake.LEFT)

            if ch == curses.KEY_UP:
                snake.set_direction(snake.UP)

            if ch == curses.KEY_DOWN:
                snake.set_direction(snake.DOWN)

            # @todo convert to arena.move_entities()

            snake.move()

            self.arena.process_collisions()

