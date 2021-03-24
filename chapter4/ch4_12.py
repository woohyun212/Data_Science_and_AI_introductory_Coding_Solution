import random
options = ['왼쪽', '중앙', '오른쪽']
computer_choice = random.choice(options)

user_choice = input("어디를 공격하시겠어요?(왼쪽, 중앙, 오른쪽) : ")
if computer_choice == user_choice:
    print("공격에 실패하셨습니다.")
else:
    print("공격에 성공하셨습니다.")
print('컴퓨터의 수비위치 :',computer_choice)