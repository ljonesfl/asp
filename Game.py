import curses
from Keyboard import Keyboard
from Serpent import Serpent
from random import randint


class Game(object):
    def __init__(self, screen):
        self.screen = screen

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

        while True:
            ticks = ticks + 1

            ch = keyboard.get()

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

            snake.move()

