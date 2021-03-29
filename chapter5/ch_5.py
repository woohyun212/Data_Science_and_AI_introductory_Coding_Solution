import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")

n = int(turtle.textinput("", "몇각형을 원하시나요?"))
l = int(turtle.textinput("", "한 변의 길이는?"))

for i in range(n):
    turtle1.forward(l)
    turtle1.left(360/n)

turtle.done()
