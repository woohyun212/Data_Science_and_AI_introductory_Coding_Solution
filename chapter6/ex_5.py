def cel2fah(celsius):
    fahrenheit = (9 / 5 * celsius) + 32
    return fahrenheit


for i in range(0, 51, 10):
    print(f"섭씨 온도 : {i:3} 도, 화씨온도 : {cel2fah(i):3} 도")
