from math import pi, fabs

Cube = lambda side: side ** 3
# 정육면체: cube / 변: side
Cuboid = lambda width, height, length: width * height * length
# 직육면체: Cuboid /가로: width / 높이: height / 깊이(길이): length
Cone = lambda radius, height, pi: pi * radius ** 2 * height / 3
# 원뿔: Cone / 반지름: radius
Sphere = lambda radius, pi: pi * 4 / 3 * radius
# 구 : sphere
Cylinder = lambda radius, height, pi: pi * (radius ** 2) * height
# 윈기둥 : cylinder
print("(1) 모서리 길이가 13인 정육면체 : ", Cube(13))
print("(2) 모서리 길이가 22인 정육면체 : ", Cube(22))
print("(3) 가로, 세로, 길이가 각각 17, 25, 16인 직육면체 :", Cuboid(17, 25, 16))
print("(4) 반지름과 높이가 각각 10, 15인 원뿔 :", Cone(10, 15, 3.14))
print("(5) 반지름이 25인 구 :", Sphere(25, 3.14))
print("(6) 반지름과 높이가 각각 10, 15인 원기둥 :", Cylinder(10, 15, 3.14))
print("(7) (4) :", Cone(10, 15, pi))
print("(7) (5) :", Sphere(25, pi))
print("(7) (6) :", Cylinder(10, 15, pi))
