n = int(input("세 자리 정수를 입력하시오 : "))
print(n % 10,end="")
print((n // 10) - ((n // 100) * 10),end="")
print(n // 100,end="")
