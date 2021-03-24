def circumference(radius):
    return 2 * radius * 3.14


def area(radius):
    return radius * 2 * 3.14


radius = 20
print("피자의 둘레는", round(circumference(radius), 2), "피자의 면적은", round(area(radius), 2))
radius = 30
print("피자의 둘레는", round(circumference(radius), 2), "피자의 면적은", round(area(radius), 2))
