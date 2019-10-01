import time
import sys
import curses

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

        self.window = self.screen.create_window()
        self.keyboard = Keyboard(self.window)
        self.levels = []
        self.init_levels()

        if len(sys.argv) > 1:
            self.current_level = int(sys.argv[1])
        else:
            self.current_level = 1

        self.arena = Arena(self.window)

    def init_levels(self):
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

        paused = False

        self.start_screen()

        self.arena.set_level(self.levels[self.current_level-1])

        while True:
            ticks = ticks + 1

            ch = self.keyboard.get()

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
                self.game_over_screen(end.message)

            except LevelCompleted:
                self.level_completed_screen()
                self.next_level()

    def next_level(self):
        self.current_level += 1
        if self.current_level > len(self.levels):
            self.window.clear()
            print("You beat the game!")
            exit()

        self.arena.set_level(self.levels[self.current_level - 1])

    def level_completed_screen(self):
        self.window.clear()
        self.screen.screen.refresh()
        self.window.center_text(int(self.window.height / 2), "Level " + str(self.current_level) + " Completed")
        self.window.center_text(int(self.window.height / 2) + 5, "Current Score: " + str(self.arena.score) + " ")

        self.get_key()
        self.window.clear()

    def get_key(self):
        while self.keyboard.get() <= 0:
            time.sleep(1)

    def game_over_screen(self, message):
        self.window.clear()
        self.window.center_text(int(self.window.height / 2), "Game Over")
        self.window.center_text(int(self.window.height / 2) + 5, message)
        self.window.center_text(int(self.window.height / 2) + 10, "Final Score: " + str(self.arena.score) + " ")

        self.get_key()
        self.window.clear()
        exit()

    def start_screen(self):
        self.window.clear()
        self.screen.screen.refresh()
        self.window.center_text(int(self.window.height / 2), "ASP")
        self.window.center_text(int(self.window.height / 2) - 10, "Designed by Abigail Jones")
        self.window.center_text(int(self.window.height / 2) - 5, "Programmed by Lee Jones")
        self.window.center_text(int(self.window.height / 2), "Press 'p' to pause")
        self.window.center_text(int(self.window.height / 2) + 5, "Press 'q' to quit")
        self.window.center_text(int(self.window.height / 2) + 10, "Press any key to start")

        self.get_key()
        self.window.clear()
