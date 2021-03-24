import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(1)
turtle1.shapesize(3, 3)
while 1:
    character = input("명령을 입력하시오 : ")
    if character == 'l':
        turtle1.left(90)
        turtle1.forward(100)
    elif character == 'r':
        turtle1.right(90)
        turtle1.forward(100)
    elif character == 'f':
        turtle1.forward(100)
