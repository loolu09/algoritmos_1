
numero = int(input('Digite um numero: '))
soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

if numero == soma_divisores:
    print('É um numero perfeito')
else:
    print('Não é um numero perfeito')
