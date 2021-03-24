num = list(map(int, input("세 정수를 입력하시오 : ").split(" ")))
num.sort()
for i in range(len(num)):
    print(num[i], end=" ")
