from Screen import Screen
from Keyboard import Keyboard
from Game import Game

screen = Screen()
window = screen.create_window()

game = Game(window, Keyboard(window))

game.play()
