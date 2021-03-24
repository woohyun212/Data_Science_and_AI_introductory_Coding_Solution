import random, turtle

turtle1 = turtle.Turtle()
turtle1.shape("turtle")

random_list = []
for i in range(10):
    random_list.append(random.randrange(2))
    if random_list[i] == 0:
        turtle1.right(90)
        turtle1.forward(50)
    elif random_list[i] == 1:
        turtle1.left(90)
        turtle1.forward(50)
print(random_list)
turtle.done()
