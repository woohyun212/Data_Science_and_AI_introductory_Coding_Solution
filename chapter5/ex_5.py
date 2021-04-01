# depth : 30M, Snail : 7 M/day,
moving_distance = 0
day = 1
while moving_distance < 30:
    moving_distance += 7  # 하루의 시작
    print('day : {:3} 달팽이의 위치 : {:3} 미터'.format(day, moving_distance))  # 저녁
    if moving_distance >= 30:
        break
    moving_distance -= 5  # 밤
    day += 1  # 다음날
print("축하합니다. 우물을 탈출하였습니다.")
print("우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day))

