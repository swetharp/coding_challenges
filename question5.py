from math import pi
def per_area(radius):
    perimeter = 2 * pi * radius,4
    area = pi * radius**2, 4
    print(f"perimeter of the the circle with radius equal to {radius} is {perimeter: .4f}")
    print(f"area of the circle with radius {radius} is {area: .4f}")
    
per_area(4)