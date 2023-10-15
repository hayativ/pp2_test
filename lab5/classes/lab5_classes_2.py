class Shape(object):
    def __init__(self) -> None:
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l : int) -> None:
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

l = int(input())
result = Square(l)
print(result.area())