
'''
pensando em listas de 50 listas, onde serao lidas (random) 4 notas (0 - 100) mostre:
    a % de alunos aprovados
    a % de alunos reprovados

    imprima os 5 primeiros alunos com a media mais alta
    imprima os 5 piores alunos
    imprima a nota mais alta, a posicao e qual aluno pertence
'''
import random

listas_notas = []

for _ in range(50):
    notas = [ ]
    for _ in range(4):
        notas.append(random.randint(0, 100))
    listas_notas.append(notas)

print(listas_notas)