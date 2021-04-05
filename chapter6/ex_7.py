def factorial(n):
    for i in range(1, n):
        n *= i
    return n


print(factorial(5), factorial(7), factorial(10))
