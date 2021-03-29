import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")

# Drawing Equilateral triangle
for i in range(3):
    turtle1.forward(100)
    turtle1.left(360/3)

# Moving turtle1 to drawing Square

turtle1.penup()
turtle1.goto(200, 0)
turtle1.pendown()

# Drawing Square
for i in range(4):
    turtle1.forward(100)
    turtle1.left(360/4)

# Moving turtle1 to drawing Regular Hexagon

turtle1.penup()
turtle1.goto(-200, 0)
turtle1.pendown()

# Drawing Regular Hexagon
for i in range(6):
    turtle1.forward(100)
    turtle1.left(360/6)

turtle.done()
