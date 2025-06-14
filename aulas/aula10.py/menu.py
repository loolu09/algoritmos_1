
from util import limpar_tela

# def ler_opcao(lim_sup):
#     op = input('Escolha uma opção: ')

#     if op >= 0 and op <= lim_sup:
#         return op
#     print('vc n digitou uma opcao valida')
#     return -1

def ler_opcao(lim_sup, lim_inf=0):
    while True:
        try:
            op = int(input('Escolha uma opção: '))
            if lim_inf <= op <= lim_sup:
                return op
            else:
                print(f'Você deve digitar um número entre {lim_inf} e {lim_sup}.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')

def menu_principal():
    limpar_tela()
    
    print('-----MENU-----')
    print('1- Cadastrar')
    print('2- Matricular')
    print('3- Consultar')
    print('4- Relatório')
    print('0- Sair')
    ler_opcao(4)

def menu_cadastro():
    limpar_tela()

    print('----MENU----')
    print('1- Aluno')
    print('2- Professor')
    print('3- Turma')
    print('0- Voltar')
    ler_opcao(3)


def matricular():
    limpar_tela()
    print('-----Matrícula de Aluno-----')
    print('1- Aluno')
    print('0- Voltar')
    ler_opcao(1)

