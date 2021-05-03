import numpy as np

print('# 1)')
n_arr = np.arange(25).reshape(5, 5)
print(n_arr)

print('# 2)')
print('첫 원소 :', n_arr[0][0])
print('마지막 원소 :', n_arr[-1][-1])

print('# 3)')
a_arr = n_arr[:2]
print(a_arr)

print('# 4)')
a_arr = n_arr[2:]
print(a_arr)

print('# 5)')
a_arr = n_arr[::, ::2]
print(a_arr)

print('# 6)')
a_arr = n_arr[::2, ::2]
print(a_arr)

print('# 7)')
a_arr = n_arr[:2:].reshape(5, 2)
print(a_arr)
