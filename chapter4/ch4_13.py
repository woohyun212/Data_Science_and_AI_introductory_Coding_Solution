import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")


def rectangle(width, height):
    for _ in range(2):
        turtle1.forward(width)
        turtle1.left(90)
        turtle1.forward(height)
        turtle1.left(90)


def triangle(width, height):
    turtle1.forward(width)
    turtle1.goto(width / 2, height)
    turtle1.goto(0, 0, )


shape = turtle.textinput("", "도형을 입력하시오")
if shape == '사각형':
    width, height = map(float, turtle.textinput(" ", "폭과 높이를 입력하시오").split(" "))
    rectangle(width, height)
elif shape == '삼각형':
    width, height = map(float, turtle.textinput(" ", "폭과 높이를 입력하시오").split(" "))
    triangle(width, height)
elif shape == '원':
    radius = float(input(turtle.textinput(" ", "반지름을 입력하시오")))
    turtle1.circle(radius)

turtle.done()
