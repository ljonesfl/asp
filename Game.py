import curses
import time

from Keyboard import Keyboard
from Arena import Arena
from Level import Level
from MovingEntity import MovingEntity
from Exceptions import GameOver
from Exceptions import LevelCompleted


class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.arena = None

        level1 = Level()

        level2 = Level()
        level2.initial_length = 20
        level2.entities = 50
        level2.poison_ratio = 7
        level2.snack_growth_factor = 3
        level2.initial_snake_friction = 45

        level3 = Level()
        level3.initial_length = 30
        level3.entities = 75
        level3.poison_ratio = 5
        level3.snack_growth_factor = 5
        level3.initial_snake_friction = 40

        level4 = Level()
        level4.initial_length = 40
        level4.entities = 100
        level4.poison_ratio = 5
        level4.snack_growth_factor = 7
        level4.initial_snake_friction = 35

        self.levels = [
            level1,
            level2,
            level3,
            level4
        ]

    def play(self):
        ticks = 0
        level = 1
        window = self.screen.create_window()
        keyboard = Keyboard(window)

        self.arena = Arena(window)

        self.arena.set_level(self.levels[level-1])

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

            except GameOver as end:
                self.screen.clear()
                self.screen.screen.refresh()
                window.center_text(int(window.height/2), "Game Over")
                window.center_text(int(window.height/2) + 5, end.message)
                window.center_text(int(window.height/2) + 10, "Final Score: " + str(self.arena.score) + " ")
                while keyboard.get() <= 0:
                    time.sleep(1)

                exit()

            except LevelCompleted:
                self.screen.clear()
                self.screen.screen.refresh()
                window.center_text(int(window.height/2), "Level " + str(level) + " Completed")
                window.center_text(int(window.height/2) + 5, "Current Score: " + str(self.arena.score) + " ")
                while keyboard.get() <= 0:
                    time.sleep(1)

                self.screen.clear()
                self.screen.screen.refresh()

                level += 1

                if level > len(self.levels):
                    self.screen.clear()
                    self.screen.screen.refresh()
                    print("You beat the game!")
                    exit()

                self.arena.set_level(self.levels[level-1])

