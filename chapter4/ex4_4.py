x = int(input("정수를 입력하시오 : "))
if x % 2 != 0:
    print(str(x) + "는(은) 2(으)로 나누어지지 않습니다.")
    able_to_divide2 = False
else:
    print(str(x) + "는(은) 2(으)로 나누어집니다.")
    able_to_divide2 = True
if x % 3 != 0:
    print(str(x) + "는(은) 3(으)로 나누어지지 않습니다.")
    able_to_divide3 = False
else:
    print(str(x) + "는(은) 3(으)로 나누어집니다.")
    able_to_divide3 = True

if able_to_divide2 and able_to_divide3:
    print(str(x) + "는(은) 2와(과) 3 모두로 나누어집니다.")
else:
    print(str(x) + "는(은) 2와(과) 3 모두로 나누어지지 않습니다.")