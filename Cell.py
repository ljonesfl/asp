

class Cell(object):
    def __init__(self, x, y, color, parent):
        self.x = x
        self.y = y
        self.color = color
        self.parent = parent

    def __str__(self):
        return "x %s, y %s, parent %s" % (self.x, self.y, self.parent)
