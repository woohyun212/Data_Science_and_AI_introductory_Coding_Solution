def distance(x1, y1, x2, y2):
    return (((x1-x2)**2)+((y1-y2)**2))**(1/2)


x1 = float(input("x1 : "))
y1 = float(input("y1 : "))
x2 = float(input("x2 : "))
y2 = float(input("y2 : "))

print(f'({x1}, {y1})과 ({x2}, {y2}) 사이의 거리는 {distance(x1,y1,x2,y2)}')