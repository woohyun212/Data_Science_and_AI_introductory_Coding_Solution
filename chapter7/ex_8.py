n = int(input("n을 입력하시오 : "))
i, line_num = 1, 1
for _ in range(n):
    if line_num % 2 == 1:
        for _ in range(n):
            print(f'{i:>3}', end=" ")
            i += 1
    else:
        i += n
        for _ in range(n):
            print(f'{i:>3}', end=" ")
            i -= 1
        i += n + 2
    line_num += 1
    i -= 1
    print()
