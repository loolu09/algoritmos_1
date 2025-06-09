import math
#como trabalhar com datas no python

'''
lambda function

def nome(x, y. z)
    corpo da func

sintaxe: lambda argumentos: expressao

'''
dobro = lambda x: x * 2 #lambda sozinho nao serve para muita coisa
print('exemplo -1 Dobro de 5', dobro(5))


soma = lambda x, y: x + y
print('Exemplo-2 Soma de 3 e 4', soma(3, 4))

hipotenusa = lambda x, y: (x**2 + y**2)** 0.5 
#hipo = lambda a, b: math.sqrt(a**2 + b**2)
print('Exemplo - 3 A raiz da hipotenusa do triangulo é', hipotenusa(3, 4))

# filter, map, reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print('exemplo - 4 numeros pares: ', pares)


quadrado = list(map(lambda x: x**2, numeros))
print('exemplo - 5 Quadrado dos numeros', quadrado)

#sorted(pessoas, key = lambda x: x[1])
pessoas = [('Ana', 20), ('João', 30), ('Maria', 20)]
