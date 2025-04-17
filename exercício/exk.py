
n = int(input('Digite um número: '))
soma = 0

for i in range(n + 1):
    termo = i / (2 * i - 1)
    soma += termo
print(f'A soma da serie do numero {n} é {soma} ')