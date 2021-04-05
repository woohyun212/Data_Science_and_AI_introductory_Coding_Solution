def sort(n1, n2, n3):
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n2 > n3:
        n2, n3 = n3, n2
    return n1, n2, n3


def max_and_min(n1, n2, n3):
    array = sort(n1, n2, n3)
    return array[2], array[0]


n1, n2, n3 = map(int, input("3 수를 입력하시오 : ").split())
print(f'가장 큰 수 : {max_and_min(n1, n2, n3)[0]}')
print(f'가장 작은 수 : {max_and_min(n1, n2, n3)[1]}')
