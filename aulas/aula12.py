
#map, filter e reduce

from functools import reduce

'''
sintaxe
    reduce(func, array)
    
'''



# numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# soma_total = reduce(lambda x, y: x + y, numeros, 100)

# print(soma_total)

from random import randint

numeros = [randint(1, 500) for _ in range(10)]

maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior) 



