class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


areas = Rectangle(3, 4)
print(areas.area())
