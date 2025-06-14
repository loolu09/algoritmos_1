
professores = []

def cadastrar_prof():
    #  {cpf: 123, nome: fulano, endereco: rua x e mais dois campos}
    professor = {'cpf': 123, 'nome': 'beto', 'end': {'rua': 'rua x'}, 'titulacao': '123123'}
    professores.append(professor)

def listar_professores():
    print(professores)