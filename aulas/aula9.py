
lista = [1, 2, 3, 4, 5]
quadrado = [num**2 for num in lista]
pares = [x for x in lista if x % 2 == 0]
print(quadrado) 


def soma(x, y): #pode usar a variavel que quiser
    resultado = x + y
    
    return resultado, x, y

resultado = soma(2, 3) #necessario para chamar uma funcao

# procedimento é uma chamada

def subtracao(x, y):
    return x - y

resultado = subtracao(2, 3)

def multiplicacao(x, y):
    return x * y

resultado = multiplicacao(2, 3)

def divisao(x, y):
    return x / y

resultado = divisao(4, 2)

