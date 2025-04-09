# LAÇOS DE REPETIÇÃO

'''
-> para nao entrar em loop infinito é necessário definir os seguintes passos:
- var de controle
- cond parada
- att da var de controle 
'''
'''
for i in range(1):
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    n3 = float(input('Digite a nota 3: '))
    n4 = float(input('Digite a nota 4: '))
    media = (n1 + n2 + n3 + n4) / 4
    print('Prox. aluno ---->')
'''
for i in range(20, 0, -1):
    print(i)