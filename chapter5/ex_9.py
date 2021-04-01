MAX, MIN, n, count = 0, 0, int(input("정수를 입력하시오 : ")), 0
while n != -99:
    if count == 0:
        MAX, MIN = n, n
    elif MAX < n:
        MAX = n
    elif MIN > n:
        MIN = n
    count += 1
    n = int(input("정수를 입력하시오 : "))
print(f'{count}개의 유효한 정수중 가장 큰 정수는 {MAX} 이고, 가장 작은 정수는 {MIN}입니다.')
