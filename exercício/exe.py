
num = int(input("Digite um número: "))
soma = 0

for i in range(num + 1):
    if i % 2 != 0:
        soma += i
print(soma)