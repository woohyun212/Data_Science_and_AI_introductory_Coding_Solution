import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(1)
turtle1.shapesize(3, 3)
while 1:
    character = input("명령을 입력하시오 : ")
    try:
        character = int(character)
        turtle1.shapesize(3 * character, 3 * character)
    except:
        if character == 'l':
            turtle1.left(90)
            turtle1.forward(100)
        elif character == 'r':
            turtle1.right(90)
            turtle1.forward(100)
        elif character == 'f':
            turtle1.forward(100)
        elif character == 'h':
            turtle1.shapesize(30, 30)
        elif character == 'n':
            turtle1.shapesize(3, 3)
