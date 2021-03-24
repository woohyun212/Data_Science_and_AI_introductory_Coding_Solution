average_velocity = float(input("평균시속(km/h)을 입력하세요 : "))
time = float(input("이동시간(h)을 입력하세요 : "))
distance = average_velocity * time
hour = round(time)
time -= round(time)
seconds = 3600 * time
minutes = seconds // 60
seconds %= 60

print("평균 시속 : ", average_velocity, "km/h")
print("이동 시간 : ", hour, "시간", round(minutes), "분", round(seconds), "초")
print("이동 거리 : ", distance, "km")
