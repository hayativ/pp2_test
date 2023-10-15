class InputOutString(object):
    def __init__(self) -> None:
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

result = InputOutString()
result.getString()
result.printString()