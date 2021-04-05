def sort(n1, n2, n3):
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n2 > n3:
        n2, n3 = n3, n2
    return n1, n2, n3


def max3(n1, n2, n3):
    array = sort(n1, n2, n3)

    return array[2]


def min3(n1, n2, n3):
    array = sort(n1, n2, n3)
    return array[0]


n1, n2, n3 = map(int, input("3 수를 입력하시오 : ").split())
print(f'가장 큰 수 : {max3(n1, n2, n3)}')
print(f'가장 작은 수 : {min3(n1, n2, n3)}')
