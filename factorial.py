def factorial(n):
    x = 1
    i = 1
    while i <= n:
        x = x * i
        print("i=", i)
        i = i + 1
    return x

mogo = 6
print(factorial(mogo))
#n = factorial(5)
