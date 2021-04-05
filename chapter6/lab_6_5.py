import turtle


def drawBar(height):
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.left(90)
    turtle1.forward(height)
    turtle1.write(str(height), font=('Times New Roman', 16, 'bold'))
    turtle1.right(90)
    turtle1.forward(40)
    turtle1.right(90)
    turtle1.forward(height)
    turtle1.left(90)
    turtle1.end_fill()
    turtle1.forward(15)
    turtle1.penup()


data = [120, 56, 309, 220, 156, 23, 98]
turtle1 = turtle.Turtle()
turtle1.pu()
turtle1.color("blue")
turtle1.fillcolor("red")
turtle1.pensize(3)
turtle1.backward(300)
for d in data:
    drawBar(d)

turtle.done()
