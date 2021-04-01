import time

sec = time.time()  # 1970. 1. 1
print(sec)
# d+day에서 1970년 1월 2일은 2일째 되는 날이므로 day 마지막에 1 더하기
year = 1970 + sec // (365 * 24 * 60 * 60)
day = (sec // (60 * 60) // 24) - ((sec // (365 * 24 * 60 * 60)) * 365) + 1
hour = 9 + sec // (60 * 60) % 24
min = (sec % (60 * 60)) // 60
second = int(sec % 60)
# 윤년 = 4와 400으로 나누어떨어짐, 100으로만 나누어떨어지면 아님
leapyear = 0

for i in range(1970, int(year + 1)):
    if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
        leapyear = leapyear + 1

day = day - leapyear
# 그리니치 시간에 9시간을 더할 때 33시가 등장하는 경우 대비
if hour >= 24:
    hour = hour - 24
    day = day + 1
print(day)
# 총 day 수로 달을 계산
if day <= 31:
    month = "January"
elif 31 < day <= 59:
    month = "February"
    day = day - 31
elif 59 < day <= 90:
    month = "March"
    day = day - 59
elif 90 < day <= 120:
    month = "April"
    day = day - 90
elif 120 < day <= 151:
    month = "May"
    day = day - 120
elif 151 < day <= 181:
    month = "June"
    day = day - 151
elif 181 < day <= 212:
    month = "July"
    day = day - 181
elif 212 < day <= 243:
    month = "August"
    day = day - 212
elif 243 < day <= 273:
    month = "September"
    day = day - 243
elif 273 < day <= 304:
    month = "October"
    day = day - 273
elif 304 < day <= 334:
    month = "November"
    day = day - 304
else:
    month = "December"
    day = day - 334
print(year, "years", month, day, "days", hour, "hours", min, "minutes", second, "seconds")