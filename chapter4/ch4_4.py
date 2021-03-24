import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(100)

x, y = int(turtle.textinput("", "두 정수를 입력하세요")), int(turtle.textinput("", "두 정수를 입력하세요"))
if x > 0 and y > 0:
    turtle1.goto(100, 100)

if x < 0 and y > 0:
    turtle1.goto(-100, 100)

if x < 0 and y < 0:
    turtle1.goto(-100, -100)

if x > 0 and y < 0:
    turtle1.goto(100, -100)

turtle.done()
