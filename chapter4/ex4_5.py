import random

# 입력-리스트
num = list(map(int, input("세 정수를 입력하시오 : ").split()))
# 랜덤 리스트 생성
lotto = []
for _ in range(3):
    r_num = random.randint(0, 9)
    if r_num not in lotto:
        lotto.append(r_num)

# for - if in 으로 문자확인 /count
count = 0
for i in num:
    if i in lotto:
        count += 1

# 출력
if count == 3:
    print("상금 1억원")
elif count == 2:
    print("상금 1천만원")
elif count == 1:
    print("상금 1만원")
else:
    print("다음 기회에...")
print(num)
print(lotto)