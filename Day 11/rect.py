class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
rect = Rectangle(5, 10)
area = rect.area()
perimeter = rect.perimeter()
print(f"Rectangle Width: {rect.width}, Height: {rect.height}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
