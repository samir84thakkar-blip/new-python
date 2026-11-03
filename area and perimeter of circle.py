import math


class Circle:
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle (π * r^2)."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter/circumference (2 * π * r)."""
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    try:
        user_radius =float(input("Enter the radius of the circle: "))

        if user_radius < 0:
            print("Radius cannot be negative.")
        else:
            my_circle = Circle(user_radius)
            print(f"\nResults for a circle with radius {user_radius}:")
            print(f"Area: {my_circle.area():.2f}")
            print(f"Perimeter: {my_circle.perimeter():.2f}")
    except ValueError:
        print("Please enter a valid numerical value for the radius.")
