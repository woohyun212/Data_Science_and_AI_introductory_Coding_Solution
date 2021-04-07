import random

# 10가지 문제 생성
problems = []
for i in range(10):
    problems.append(str(random.randint(100, 900)) + " + " + str(random.randint(100, 900)))
    print(problems[i])
# 랜덤으로 하나 뽑아서 출력
i = random.randint(0, len(problems) - 1)
print(f'\n{problems[i]} = {eval(problems[i])}')
