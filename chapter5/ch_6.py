import turtle, random

turtle1 = turtle.Turtle()
turtle1.shape("turtle")

for i in range(30):
    turtle1.forward(random.randint(1, 100))
    turtle1.right(90 * random.randint(1, 4))
turtle.done()
