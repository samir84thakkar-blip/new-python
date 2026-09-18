import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(231, 621)
square = turtle.Turtle()


side_length = 100
num_sides = 4
angle = 360.0 / num_sides
for i in range(num_sides):
    square.forward (side_length)
    square.right(angle)


turtle.done()
