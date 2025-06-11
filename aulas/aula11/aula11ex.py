
#gere 100 numeros randomicos (20, 100), filtrar os maiores que 60
#gere 100 numeros randomicos (20, 100), filtrar os maiores que a media
#gere 100 numeros randomicos (20, 100), filtrar os menores que 25

import random

numeros = [random.randint(20, 100) for _ in range(100)]

maior = list(filter(lambda x: x > 60, numeros))
menor = list(filter(lambda x: x < 25, numeros))

media = list(filter(lambda x: x > (sum(numeros) / len(numeros)), numeros))

print(maior)