import turtle, random

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(0)

length = 10
angle = random.randint(80, 100)
while length < 500:
    turtle1.forward(length)
    turtle1.right(angle)
    length += 5

turtle.done()
