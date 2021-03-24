try:
    number_of_compute = input("""1)덧셈 2)뺄셈 3)곱셈 4)나눗셈
어떤 연산을 원하는지 번호를 입력하세요:""")
    if number_of_compute not in ['1','2','3','4']:
        print("잘못 입력하였습니다")
    else:
        num1, num2 = map(int, input("연산을 원하는 숫자 두개를 입력하세요\n").split(" "))
        if number_of_compute == '1':
            print(num1, "+", num2, "=", num1 + num2)
        if number_of_compute == '2':
            print(num1, "-", num2, "=", num1 - num2)
        if number_of_compute == '3':
            print(num1, "*", num2, "=", num1 * num2)
        if number_of_compute == '4':
            print(num1, "/", num2, "=", num1 / num2)

except:
    print("잘못 입력하였습니다.")


