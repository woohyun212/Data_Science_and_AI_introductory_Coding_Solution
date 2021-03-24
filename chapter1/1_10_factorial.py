
def factorial(index):
    if index == 1:
        print("1 = ",end="")
        return 1
    else:
        print(str(index)+" * ",end='')
        return index * factorial(index-1)
print(factorial(10))