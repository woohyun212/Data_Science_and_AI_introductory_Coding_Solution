for _ in range(2):
    t = False
    n = int(input("정수를 입력하세요 :"))
    if 0 <= n <= 100 and n % 2 != 1:
        t = True
    print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", t)
