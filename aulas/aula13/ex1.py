def func(x):
    #caso base
    if x < 1:
        return 0
    print(x)
    return x + func(x - 1)

print(func(10))