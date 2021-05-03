import numpy as np

print('# 1)')
a = np.random.randint(1, 100, size=(3, 3, 3))
print(a)

print('# 2)')
print('a의 원소들 중 최댓값 :', a.max())

print('# 3)')
print('a의 원소들 중 최댓값의 위치 :', a.argmax())
