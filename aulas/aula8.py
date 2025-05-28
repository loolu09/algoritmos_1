
# aula de dicionario
'''
estruturas muito utilizadas
- é uma lista de associações compostas por uma chave 'unica'
- são mutáveis
- 

sintaxe basica:
dicionario = {'a':(1, 2, [1, 2, {1:20, 2:30}])} obrigatorio para declarar um dicionario

'''
dic = {'nome1':'beto', 'nome2':'ana', 'nome3':'vitor'}

dic['nota'] = 7.80 

# usando esse print para debug
print(dic)

# dic = {(1, 2, 3, 4):'beto'} pode!

#funcoes mais usuais
items = dic.items()
chaves = dic.keys()
valores = dic.values()

print(f'Items = {items}')
print(f'chaves = {chaves}')
print(f'valores = {valores}')

#get

for i, j in dic.items():
    print(f'i = {i} e j = {j}')

#compreensao de listas
lista = [i for i in range(5)] #cria uma lista
print(lista)

#pesquisa: como trabalhar com compreensao de listas
#posso colocar o que eu quiser dentro de lista = []

