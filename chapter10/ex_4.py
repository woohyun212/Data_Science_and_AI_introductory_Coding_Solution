import numpy as np

print('# 1)')
a = np.arange(1, 26).reshape(5, 5) % 2
print(a)

print('# 2)')
b = np.sum(a, axis=0)
# 행 방향 -> 세로
# 열 방향 -> 가로
print("행렬의 행 방향 성분의 합 : ")
print(b)
