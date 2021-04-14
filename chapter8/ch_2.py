items = {"커피음료": 4, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}


def getStock(_item_key):
    return items[_item_key]


def storeStock(_item_key, _quantity):
    items[_item_key] += _quantity


def releaseStock(_item_key, _quantity):
    items[_item_key] -= _quantity


while 1:
    selectedMenu = input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료 : ")
    if selectedMenu == "1" or selectedMenu == "재고조회":
        item_key = input("[재고조회] 물건의 이름을 입력하시오: ")
        print("재고 :", getStock(item_key))

    elif selectedMenu == "2" or selectedMenu == "입고":
        item_key, quantity = input("[입고] 물건의 이름과 수량을 입력하시오: ").split()
        storeStock(item_key, int(quantity))
        print(f"{items[item_key]}의 재고 :", getStock(item_key))

    elif selectedMenu == "3" or selectedMenu == "출고":
        item_key, quantity = input("[입고] 물건의 이름과 수량을 입력하시오: ").split()
        releaseStock(item_key, int(quantity))

    elif selectedMenu == "4" or selectedMenu == "종료":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 값이 입력되었습니다.")
