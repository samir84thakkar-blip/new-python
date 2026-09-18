import math


def circumference_circle(radius):
    return 2 * math.pi * radius


radius = float(input("Enter the radius of the circle: "))
print("The circumference is:", circumference_circle(radius))
    