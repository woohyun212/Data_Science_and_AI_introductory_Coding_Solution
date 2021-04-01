n, array = int(input("정수를 입력하시오 : ")), []

while n != -99:
    array.append(n)
    n = int(input("정수를 입력하시오 : "))
array.sort()
print(f'{len(array)}개의 유효한 정수중 가장 큰 정수는 {array[len(array)-1]} 이고, 가장 작은 정수는 {array[0]}입니다.')
