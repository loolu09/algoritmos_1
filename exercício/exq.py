
n = int(input('Digite um numero: '))

for i in range(2, n + 1):
    while n % i == 0:
        print(i, end='*' if n > i else '')
        n //= i