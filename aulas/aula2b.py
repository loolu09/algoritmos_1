# segunda aula de python

'''
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'Aluno aprovado com média {media}')
elif media >= 4:
    print(f'Aluno recuperação com média {media}')
else:
    print(f'Aluno reprovado com média {media}')
'''

number = int(input('Escolha um número: (1-7)'))

if number >=1 and number <=7:
    if number == 1:
        print('Domingo')
    elif number == 2:
        print('Segunda') 
    elif number == 3:
        print('Terça') 
    elif number == 4:
        print('Quarta') 
    elif number == 5:
        print('Quinta') 
    elif number == 6:
        print('Sexta') 
    else:
        print('Sábado')
            