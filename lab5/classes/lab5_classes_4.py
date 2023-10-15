import math
class Point(object):
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x : float, y : float):
        self.x += x
        self.y += y

    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

#x = int(input())
#y = int(input())