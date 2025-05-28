'''
leia o nome de 5 pessoas e armazene em um dicionario

crie um programa para gerar um dicionario com 20 numeros inteiros, mostre a soma de todos os elementos
'''

# nomes = {}

# for i in range(5):
#     nome = input(f'Digite o {i+1}º nome: ')
#     nomes[i] = nome
# print(nomes)
    
from random import randint
num = {}
soma = 0

for i in range(20):
    num[i] = randint(1, 50)
    soma+=num.get(i)

print(num)
print(soma)

'''
ex 3: crie um programa para ler o nome, matricula e as quatro notas de 5 alunos e 
armazene em um dicionario = {matricula:nome. notas: [n1, n2, n3, n4]}
as notas podem ser geradas de forma aleatoria com o uso de compreensao de listas 

a) mostrar o aluno com maior media
b) a % de alunos com media maior que 8
c) a % de alunos que estariam reprovados, considerando media < 4
'''
import random

alunos = {}

for i in range(5):
    matricula = int(input('Digite a matricula: '))
    nome = input(f'Digite o {i+1}º nome: ')
    notas = [random.randint(0, 10) for _ in range(4) ]
    alunos[matricula] = {'nome': nome, 'notas': notas}

print('\n DADOS DE ALUNOS')
print(alunos)

print('\n MÉDIA DOS ALUNOS')

maior_media = -1
aluno_maior = ''
acima_8 = 0
reprovado = 0

for matricula, dados in alunos.items():
    notas = dados['notas']  
    media = sum(notas) / len(notas)
    print(print(f"{dados['nome']} ({matricula}) - Notas: {notas} - Média: {media:.2f}"))
    
    if media >= maior_media:
        maior_media = media
        aluno_maior = dados['nome']

    if media > 8:
        acima_8 += 1
    if media < 4:
        reprovado += 1

print(f'Aluno com maior média: {aluno_maior}({maior_media:.2f})')
print(f'% de alunos com média > 8: {(acima_8 / 5) * 100:.1f}%')
print(f'A % de alunos reprovados é: {(reprovado / 5) * 100:.1f}%')

