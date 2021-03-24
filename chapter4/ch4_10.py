from math import sqrt

x, y = map(int, (input("점의 좌표 x, y를 입력하시오 : ")).split(" "))
sqrt((3-x) ** 2 + (4-y) ** 2) 
if sqrt((3-x) ** 2 + (4-y) ** 2) > 10:
    print("원의 외부에 있음")
elif sqrt((3-x) ** 2 + (4-y) ** 2) < 10:
    print("원의 내부에 있음")
else:
    print("원 위에 있음")
