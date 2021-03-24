print("섭씨".ljust(3), "화씨".ljust(5))
for celsius in range(0,60,10):
    fahrenheit = (9 / 5) * celsius + 32
    print(str(celsius).ljust(5), str(fahrenheit).ljust(5))
