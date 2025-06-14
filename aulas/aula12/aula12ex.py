
'''
exercício 1: calcular a média dos quadrados dos números pares de uma lista
exercício 2: encontrar o maior número impar após elevar ao cubo
exercício 3: somar os quadrados dos números que são múltiplos de 3
exercicio 4: calcular o produto dos números pares após multiplicar por 2
exercício 5: encontrar a média dos números que são maiores que 5 após elevar ao quadrado
exercício 6: calcular a soma dos cubos dos números que são menores que a média da lista

'''
from random import randint
from functools import reduce

#1
numeros = [randint(1, 100) for _ in range(10)]
media = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))
print('Média dos quadrados dos pares: ', media)

#2
num = [randint(1, 20) for _ in range(10)]
impares_cubos = list(map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, num)))

if impares_cubos:
    maior_impar = reduce(lambda x, y: x if x > y else y, impares_cubos)
    print(f'O maior número ímpar é {maior_impar}')
else:
    print('Não há números ímpares')

#2.1
'''
maior_impar = max(filter(lambda x: x % 2 != 0, map(lambda x: x**3, numeros)))  
'''
#3
numbers = [randint(1, 50) for _ in range(10)]
soma_quadrados = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 3 == 0, numbers)))
print(f'O soma dos quadrados é {soma_quadrados}')

#4
n = [randint(1, 35) for _ in range(15)]
produto_pares = reduce(lambda x, y: x * y, map(lambda x: x * 2, filter(lambda x: x % 2 == 0, n)))
print(f'O produto dos pares é {produto_pares}')

#5
numero = [randint(1, 25) for _ in range(10)]
media_maior_cinco = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x > 5, numero))) / len(list(filter(lambda x: x > 5, numero)))
print(f'A média dos números maiores que cinco são {media_maior_cinco}')

#6
number = [randint(1, 20) for _ in range(15)]
media = sum(number) / len(number)

soma_cubos = sum(map(lambda x: x**3), filter(lambda x: x < media, number))