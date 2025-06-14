#fatorial de 5

def fatorial(x):
    if x < 1:
        return 1
    print(x)
    return x * fatorial(x - 1)

print(fatorial(5))