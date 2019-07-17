
class Keyboard(object):

    def __init__(self, window):
        self.window = window
        self.window.window.keypad(1)

    def __del__(self):
        self.window.window.keypad(0)

    def get(self):
        return self.window.window.getch()



