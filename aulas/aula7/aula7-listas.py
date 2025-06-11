'''
lista / tuplas / dicionarios

listas -> colecoes heterogeneas de objetos, podem ser qualquer tipo, inclusive outras listas
[0, 1, 10. 'luli', [0, 2, 3]]

listas em python sao mutaveis

lista_01 = [1, 2, 3, 4, 5]

'''
lista = [1, 2, 3, 4, 5]

print(lista)

nome = 'luli'

# #funcao que retorna o tamanho de uma coleção
print(len(nome))

progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP', 'Metalica', 'U2']

progs[3] = 'Metalica'

for i in range(len(progs)):
    print(progs[i])

# #forma 2
for prog in progs:
    print(prog)

# #incluir elemento
progs.append('Guns')

# #trocar o ultimo elemento
progs[-1] = 'Novo elemento na ultima posicao'

# #ordenar
progs.sort()

# #inverter a lista
progs.reverse()

# #PESQUISA
# #pop
# #remove
# #zip

for i, p in enumerate(progs):
    print(f'Posicao {i} e elemento = {p}')
    

