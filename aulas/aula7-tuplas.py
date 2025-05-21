
# tuplas -> semelhantes as listas, porem sao imutaveis: nao acrescentar, apagar, fazer atribuiçoes

tupla = (1, 2, 3, 4)

t1 = (1,) # tuplas de unico elemento

print(tupla[0])

for t in tupla:
    print(t)

lista = list(tupla)

lista_tupla = ([1, 2, 3], [2, 3], ('beto', 'vitor', 'rafael'))

#PESQUISA
#set
#frozenset

'''
Use set quando você precisar de uma coleção mutável de elementos únicos
Use frozenset quando você precisar de uma coleção imutável de elementos únicos, 
que possa ser usada como chave em um dicionário ou como elemento de outro conjunto.
'''

# uniao, interseccao e diferenca
'''
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União
uniao = conjunto_a.union(conjunto_b)
print(f"União: {uniao}")  # Saída: União: {1, 2, 3, 4, 5}

# Interseção
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Interseção: {intersecao}")  # Saída: Interseção: {3}

# Diferença
diferenca = conjunto_a.difference(conjunto_b)
print(f"Diferença (a - b): {diferenca}")  # Saída: Diferença (a - b): {1, 2}
'''

#o que é range? 