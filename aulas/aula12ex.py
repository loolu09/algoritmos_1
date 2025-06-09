
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

numeros = [randint(1, 100) for _ in range(10)]

media = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))
print('Média dos quadrados dos pares: ', media)


num = [randint(1, 20) for _ in range(10)]
maior = 
print(maior)


