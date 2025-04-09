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
'''
for i in range(1, 6):
    for j in range(1, i):
        print(j, end = " ")
    print('')
'''

for i in range(6, 1):
    for j in range(1, i + i):
        print(j, end="")