import random

while True:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    kind_of_exam = random.choice(['plus', 'minus'])
    if kind_of_exam == 'plus':
        if input(str(num1) + "+" + str(num2) + "=") == str(num1 + num2):
            print('잘했어요!')
        else:
            print('정답은', num1 + num2, '입니다. 다음번에는 잘할 수 있죠?')
    if kind_of_exam == 'minus':
        if input(str(num1) + "-" + str(num2) + "=") == str(num1 - num2):
            print('잘했어요!')
        else:
            print('정답은', num1 - num2, '입니다. 다음번에는 잘할 수 있죠?')
