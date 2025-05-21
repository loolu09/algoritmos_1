
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
alunos_aprovados = 0
alunos_reprovados = 0

for _ in range(50):
    notas = [ ]
    for _ in range(4):
        notas.append(random.randint(0, 100))
    listas_notas.append(notas)

    if notas > 50:
        alunos_aprovados +=1
    else:
        alunos_reprovados += 1

print(f'Alunos aprovados: {alunos_aprovados}\n Alunos reprovados: {alunos_reprovados}')
print(min(notas))
print(max(notas))