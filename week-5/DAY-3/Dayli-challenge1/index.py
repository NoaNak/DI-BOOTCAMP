import math #(seulement si on a un nombre a virgule et quon veux larrondir au chiffre dapres)

class Circle:
    def __init__(self, radius: int):
        self.radius = radius 
        self.diameter = radius * 2

    @classmethod
    def from_diameter(cls, diameter: int):
        return Circle(diameter // 2)

    def __str__(self):
        return f'Radius: {self.radius}, Diameter: {self.diameter}, Area: {self.area():.3f}'

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other_circle):
        result = Circle(self.radius + other_circle.radius)
        return result
    
    def __gt__(self, other_circle): # gt = greater than
        return self.area() > other_circle.area()

    def __eq__(self, other_circle) -> bool: # eq = equal 
        return self.area() == other_circle.area()

circle1 = Circle(2)
print(circle1)

circle2 = Circle.from_diameter(8)
print(circle2)

circle3 = circle1 + circle2
print(circle3)

print(circle1 > circle2)

circles = [circle3, circle1, circle2] 

def check_circles(circle_list: list) -> None:
    for circle in circle_list:
        print(circle)

check_circles(circles)

circles.sort()

print("AFTER SORTING")
check_circles(circles)















