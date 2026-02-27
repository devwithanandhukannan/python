from AbstractClass import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
    
r = Rectangle(10,30)
print("Area: ", r.area())
print("Perimeter: ", r.perimeter())
        