import random

tires, guess, answer = 0, 0, random.randint(1, 100)
print("1부터 100사이의 숫자를 맞추시오")
while 1:
    guess = int(input("숫자를 입력하세요 : "))
    tires += 1
    if tires > 10:
        print("시도 횟수 초과!")
        break
    if guess == answer:
        print("축하드립니다. 총 시도횟수 =", tires)
        break
    elif guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")