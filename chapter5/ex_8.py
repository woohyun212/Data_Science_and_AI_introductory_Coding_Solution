while 1:
    string = input("정수를 입력하시오 : ")
    if string == "-99":
        print("프로그램을 종료합니다.")
        break
    i, judge = 0, True
    while i <= len(string) // 2:
        if string[i] != string[len(string) - 1 - i]:
            judge = False
            break
        i += 1
    if judge:
        print("{}은(는) 거꾸로 정수입니다.".format(string))
    else:
        print("{}은(는) 거꾸로 정수가 아닙니다.".format(string))
