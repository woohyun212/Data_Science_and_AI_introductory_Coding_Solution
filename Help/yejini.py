import time, datetime
sec = int(time.time())  # 1970. 1. 1
print(datetime.datetime.today())
year, month, day, hours, minutes, seconds, count_month, thirtyOneMonth, thirtyMonth, leap_year = \
    [1970, 1, 1, 9, 0, 0, 0, [1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], False]
while sec > 60:
    sec -= 60
    minutes += 1
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours == 24:
        day += 1
        hours = 0
while day > 31:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        leap_year = True
    else:
        leap_year = False
    if month == 2:
        if leap_year:
            day -= 29
        else:
            day -= 28
    elif month in thirtyMonth:
        day -= 30
    elif month in thirtyOneMonth:
        day -= 31
    month += 1
    if month == 13:
        month = 1
        year += 1
print(year, month,day, hours, minutes, sec)
