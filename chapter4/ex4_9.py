import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
lb_x, lb_y = map(int, turtle.textinput("", "왼쪽 하단 모서리 좌표 x, y :").split(" "))
rt_x, rt_y = map(int, turtle.textinput("", "왼쪽 하단 모서리 좌표 x, y :").split(" "))
turtle1.penup()
turtle1.goto(lb_x, lb_y)
turtle1.pendown()
turtle1.goto(rt_x, lb_y)
turtle1.goto(rt_x, rt_y)
turtle1.goto(lb_x, rt_y)
turtle1.goto(lb_x, lb_y)
turtle1.penup()
u_x, u_y = map(int, turtle.textinput("", "왼쪽 하단 모서리 좌표 x, y :").split(" "))
turtle1.goto(u_x, u_y)
turtle1.dot(30)
turtle1.right(135)
turtle1.forward(50)
turtle1.left(135)
if lb_x < u_x < rt_x and lb_y < u_y < rt_y:
    turtle1.write("점은 사각형 내부에 있습니다.")
else:
    turtle1.write("점은 사각형 외부에 있습니다.")

turtle.done()
