total = 0
start = int(input("시작 정수를 입력하세여 : "))
end = int(input("끝 정수를 입력하세여 : "))
for i in range(start, end + 1):
    total += i
print(start, "에서", end, "까지 정수의 합 :", total)
