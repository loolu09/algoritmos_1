
num = int(input('Digite um numero: '))
fatorial = 0

for i in range(1, num + 1):
    fatorial = i * (i-1)
print(fatorial)