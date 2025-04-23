
n = int(input('Digite um numero: '))

for i in range(1, n + 1):
    linha = ''
    for j in range(1, i + 1): #o que vai imprimir com i
        linha += str(j)
    for j in range(i - 1, 0, -1): #continuaçao para virar um palindromo
        linha += str(j)

    espacos = ' ' * (n - i) #espaçamento para formar a piramide
    print(espacos + linha)