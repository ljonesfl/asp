"""
To specify a level, pass it an integer as the first argument.

python3 asp.py 4
"""

from Screen import Screen
from Keyboard import Keyboard
from Game import Game

screen = Screen()
window = screen.create_window()

game = Game(window, Keyboard(window))

game.play()
