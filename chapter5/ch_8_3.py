import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(10)
i = 0
turtle1.pu()
turtle1.goto(-150,100)
turtle1.pd()
while i < 5:
    turtle1.forward(150)
    turtle1.left(72)
    turtle1.forward(150)
    turtle1.right(144)
    i += 1
turtle.done()
