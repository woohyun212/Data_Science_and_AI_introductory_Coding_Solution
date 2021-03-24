second = int(input('초를 입력하세요 : '))
minute = second//60
second %= 60
hour = minute//60
minute %= 60
print("입력한 시간은 ",hour,"시간",minute,"분",second,"초 입니다.")