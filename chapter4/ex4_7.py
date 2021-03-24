import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)

number = int(input(str(n1) + " + " + str(n2) + " = "))
if number == n1 + n2:
    print('잘했어요!!!')
else:
    print('정답은 %d 입니다' % (n1 + n2))
