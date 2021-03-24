print('''우리식당에 오신것을 환경합니다. 메뉴는 다음과 같습니다.
- 햄버거(입력 b)
- 치킨(입력 c)
- 피자(입력 p)''')
menu = input("메뉴를 선택하세요(알파벳 b, c, p 입력 : ")
if menu == 'b':
    print("햄버거를 선택하였습니다.")
elif menu == 'c':
    print("햄버거를 선택하였습니다.")
elif menu == 'p':
    print("피자를 선택하였습니다.")
else:
    print("선택한 메뉴가 없습니다.")
