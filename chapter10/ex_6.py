import numpy as np

x1 = [i for i in range(100)]
x2 = [i + np.random.randint(1, 10) for i in range(100)]
x3 = [i + np.random.randint(1, 50) for i in range(100)]
x4 = [np.random.randint(1, 100) for i in range(100)]
x1_cor = list(np.corrcoef([x1, x2, x3, x4])[0, 1:4])
max_index = x1_cor.index(max(x1_cor))
min_index = x1_cor.index(min(x1_cor))
print("가장 상관관계가 높은 리스트")
if max_index == 0:
    print('x2')
elif max_index == 1:
    print('x3')
elif max_index == 2:
    print('x4')
print("가장 상관관계가 낮은 리스트")
if min_index == 0:
    print('x2')
elif min_index == 1:
    print('x3')
elif min_index == 2:
    print('x4')
