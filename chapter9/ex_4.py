a = input('a = ')
b = input('b = ')
for i in range(len(a)):
    print(a[i]+b[i], end='')
print()
for i in range(len(a)):
    print(a[i]+b[-i-1], end='')
