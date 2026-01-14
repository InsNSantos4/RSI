#Ficha9 Ex07

# Pretende fazer uma aplicação informática para facilitar a gestão de uma instituição de ensino.
# A sua aplicação deverá ler uma lista das cadeiras em funcionamento na instituição.
# Posteriormente, deverá perguntar ao utilizador os nomes dos alunos e, para cada aluno, a lista das cadeiras em que este se encontra inscrito (apenas cadeiras em funcionamento). Esta informação deverá constituir um dicionário (nome de aluno, lista de cadeiras em que se encontra inscrito).
# Uma vez construído o dicionário, apresente-o no ecrã, bem como as listas de alunos e de cadeiras.
# Exemplo:
# dic = {'pedro':['iprp','er'],'ana':['so'],'paula':['er','so','am']}
# cadeiras = ['iprp','er','so','am']
# alunos = ['pedro','ana','paula']
# a) Altere a sua aplicação de forma a permitir ao utilizador acrescentar cadeiras e alunos.
# b) Dê ao utilizador a possibilidade de retirar um aluno do dicionário.
# c) Acrescente na sua aplicação a possibilidade de eliminar uma cadeira.
# Neste caso, deverá eliminar todas as ocorrências da cadeira eliminada, no dicionário.

# alunos = list()
# cadeiras = list()
# inscricoes = dict()

inscricoes = {'pedro': ['iprp', 'er'], 'ana': ['so'], 'paula': ['er', 'so', 'am']}
cadeiras = ['iprp', 'er', 'so', 'am']
alunos = ['pedro', 'ana', 'paula']

while True:
    print()
    print("1 - Adicionar aluno")
    print("2 - Adicionar cadeira")
    print("3 - Associar cadeira a aluno")
    print("4 - Retirar cadeira a aluno")
    print("5 - Apagar aluno")
    print("6 - Apagar cadeira")
    print("7 - Imprimir dados")
    print("0 - Sair")

    option = input("Escolha uma das opções: ")

    if option == '0':  # Sair
        break
    elif option == '1':  # Adicionar aluno
        aluno = input("Insira o nome do aluno: ")
        if aluno in alunos:
            print("O aluno inserido já existe.")
        else:
            alunos.append(aluno)
    elif option == '2':  # Adicionar cadeira
        cadeira = input("Insira o nome da cadeira: ")
        if cadeira in cadeiras:
            print("A cadeira inserida já existe.")
        else:
            cadeiras.append(cadeira)
    elif option == '3':  # Associar cadeira a aluno
        aluno = input("Insira o nome do aluno: ")
        cadeira = input("Insira o nome da cadeira: ")
        if not (aluno in alunos):
            print("O aluno inserido não existe.")
        elif not (cadeira in cadeiras):
            print("A cadeira inserida não existe.")
        elif not (aluno in inscricoes.keys()):
            inscricoes[aluno] = [cadeira]  # aluno adicionado a inscrições e inclusão de cadeira cadeira
        elif cadeira in list(inscricoes[aluno]):
            print("A cadeira", cadeira, "já está associada ao aluno", aluno)
        else:
            inscricoes[aluno] = list(inscricoes[aluno]).append(cadeira)
            print("A cadeira", cadeira, "foi associada ao aluno", aluno, "com sucesso.")
    elif option == '4':  # Retirar cadeira a aluno
        aluno = input("Insira o nome do aluno: ")
        cadeira = input("Insira o nome da cadeira: ")
        if not (aluno in alunos):
            print("O aluno inserido não existe.")
        elif not (cadeira in cadeiras):
            print("A cadeira inserida não existe.")
        elif not (aluno in inscricoes.keys()):
            print("O aluno", aluno, "não tem cadeiras associadas.")
        elif cadeira in list(inscricoes[aluno]):
            cadeirasAluno = list(inscricoes[aluno])
            index = cadeirasAluno.index(cadeira)
            del cadeirasAluno[index]
            inscricoes[aluno] = cadeirasAluno
            print("A cadeira", cadeira, "foi desassociada do aluno", aluno, "com sucesso.")
        elif not (cadeira in list(inscricoes[aluno])):
            print("O", aluno, " não está inscrito na cadeira", cadeira)
    elif option == '5':  # Apagar aluno
        aluno = input("Insira o nome do aluno: ")
        if aluno in alunos:
            del inscricoes[aluno]
            index = alunos.index(aluno)
            del alunos[index]
            print("O aluno", aluno, "apagado com sucesso.")
        else:
            print("O aluno inserido não existe.")
    elif option == '6':  # Apagar cadeira
        cadeira = input("Insira o nome da cadeira: ")
        if not (cadeira in cadeiras):
            print("A cadeira inserida não existe.")
        else:
            index = cadeiras.index(cadeira)
            del cadeiras[index]
            for key in inscricoes.keys():
                if cadeira in list(inscricoes[key]):
                    cadeirasAluno = list(inscricoes[key])
                    index = cadeirasAluno.index(cadeira)
                    del cadeirasAluno[index]
                    inscricoes[key] = cadeirasAluno

            print("Cadeira", cadeira, "apagada com sucesso.")

    elif option == '7':  # Imprimir dados
        print(alunos)
        print(cadeiras)
        print(inscricoes)
    else:
        print("Opção inválida.")

