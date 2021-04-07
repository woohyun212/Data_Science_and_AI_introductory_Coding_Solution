def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        # 1과 자기 자신으로만 나누어 진다 <=> 1과 자기 자신 이외에도 나누어진다.
        if n % i == 0:
            return False
    return True


while 1:
    num = int(input("소수 검사를 할 정수를 입력하시오:"))
    print(f'소수인가요? {isPrime(num)}')
