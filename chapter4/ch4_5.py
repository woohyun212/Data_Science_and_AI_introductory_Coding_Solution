import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(100)

x, y = map(int, turtle.textinput('1', "두 정수를 입력하세요").split(" "))
if x > y:
    turtle1.goto(100, 0)
elif x < y:
    turtle1.goto(-100, 0)
else:
    turtle1.goto(0, 100)
turtle.done()
