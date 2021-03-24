import random

player1 = input("player1의 이름 : ")
player2 = input("player2의 이름 : ")

string = "...주사위를 굴립니다....."

p1dice = random.randint(1, 6)
p2dice = random.randint(1, 6)
print(player1 + "의 주사위 번호는", p1dice)
print(player2 + "의 주사위 번호는", p2dice)

if p1dice > p2dice:
    print(player1 + "이 이겼습니다.")
if p1dice < p2dice:
    print(player2 + "이 이겼습니다.")
