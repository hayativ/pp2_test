class Rectangle(object):
    def __init__(self, l : int, w : int) -> None:
        self.length = l
        self.width  = w

    def area(self):
        return self.length * self.width
    
length = int(input())
width = int(input())
result = Rectangle(length, width)
print(result.area())