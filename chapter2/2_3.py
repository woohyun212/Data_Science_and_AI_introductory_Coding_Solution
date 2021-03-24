import turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.speed(100)

radius = 100
turtle1.circle(radius)
turtle1.circle(radius*2)
turtle1.circle(radius/2)
turtle1.left(90)
turtle1.circle(radius)
turtle1.circle(radius*2)
turtle1.circle(radius/2)

turtle.done()