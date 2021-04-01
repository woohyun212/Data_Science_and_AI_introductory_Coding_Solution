print("세 자리의 암스트롱 수 :", end=" ")
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            if x * 100 + y * 10 + z == x ** 3 + y ** 3 + z ** 3:
                print(x * 100 + y * 10 + z, end=" ")
