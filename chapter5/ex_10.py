import turtle, random

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
i = 0
while i < 30:
    if random.randrange(2) == 0:
        turtle1.left(90)
        turtle1.forward(50)
    else:
        turtle1.right(90)
        turtle1.forward(50)
    i += 1
turtle.done()
