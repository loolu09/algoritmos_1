
'''
1- var de controle
2- condicao da parada
3- att da var de controle
'''
#var de controle
# i = 0
# #cond de parada
# while i < 10:
#     if i % 2 == 0:
#         print(f'i = {i}')
#         #att da var
#     i = i + 1 #incremento

#criar um laco com while que dependa da resposta do user p continuar o laco
resp = 's'
while resp == 's':
    print('Ainda estou repetindo...')
    while True:
        resp = input('Deseja continuar? (s) = sim / (n) = nao ')
        resp = resp.lower()
        if resp == 's' or resp == 'S' or resp == 'n' or resp == 'N':
            break
print('Terminei')