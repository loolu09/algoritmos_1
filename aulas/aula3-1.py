# EXERCÍCIO
'''
1-
ler dois numeros onde o 1 vai ser o inicio do laço e o 2 o fim.
validar os numeros de entrada (prestar atençao na validação)

2-
    *
   **
  ***
 ****
*****

'''
'''
num1 = int(input('Digite o início: '))
num2 = int(input('Digite o fim: '))

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

for i in range(num1, num2):
    print(i)
'''

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print('')

# n= 5

# for i in range(n, 0, -1):
#     espacos = (6 - i) * 2
#     print(" " * espacos, end=" ")
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print(" ")

# n= 6

# for i in range(n, 0, -1):
#     espacos = n - i
#     print(" " * espacos + "* " * i)

#4 - ler um mes e um ano qualquer, exibir o calendario completo com os dias da semana

import calendar 

#pedir o ano e o mês para o usuario
ano = int(input('Digite o ano que deseja: '))
mes = int(input('Digite o mês que deseja: '))

print('Seg Ter Qua Qui Sex Sab Dom') #printar os dias da semana

inicio, total_dias = calendar .monthrange(ano, mes) #inicio= dia q começa a semana (sera de 0 a 6) e total sao os dias do mes
espacos = '    ' * inicio
print(espacos, end='')

for dia in range(1, total_dias + 1):
    print(f'{dia:>3} ', end='') #: inicia a formataçao- >manda alinhar a direita e 3 indica o numero de espaços que deve ter

    if (inicio + dia) % 7 == 0: #saber se completou uma semana de 7 dias para quebrar a linha 
        print()