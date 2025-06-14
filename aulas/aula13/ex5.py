
#ex2 = potencia: implemente uma função recursiva que calcula a ^ b, onde a e b sao inteiros e b >= 0

def pot(a, b):
    if b <= 0:
        return 1
    return a * pot(a, b - 1)

print(pot(2, 2))