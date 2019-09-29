import curses
import time

from Keyboard import Keyboard
from Arena import Arena
from Level import Level
from MovingEntity import MovingEntity
from Exceptions import GameOver


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.arena = None

    def play(self):
        ticks = 0
        window = self.screen.create_window()
        keyboard = Keyboard(window)

        self.arena = Arena(window)

        level = Level()

        self.arena.set_level(level)

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
                self.arena.player1.set_direction(MovingEntity.RIGHT)

            if ch == curses.KEY_LEFT:
                self.arena.player1.set_direction(MovingEntity.LEFT)

            if ch == curses.KEY_UP:
                self.arena.player1.set_direction(MovingEntity.UP)

            if ch == curses.KEY_DOWN:
                self.arena.player1.set_direction(MovingEntity.DOWN)

            try:
                self.arena.tick()

            except GameOver:
                self.screen.clear()
                self.screen.screen.refresh()
                window.center_text(int(window.height/2), "Game Over")
                window.center_text(int(window.height/2) + 5, "Final score: " + str(self.arena.score) + " ")
                while keyboard.get() <= 0:
                    time.sleep(1)

                exit()
