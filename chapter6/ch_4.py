def get_square(a, b, c):
    return a ** 2, b ** 2, c ** 2


a, b, c = 1, 2, 3
a_sq, b_sq, c_sq = get_square(a, b, c)
print(f'{a}의 제곱 :{a_sq}, {b}의 제곱 :{b_sq}, {c}의 제곱 : {c_sq}')
