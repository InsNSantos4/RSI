# Ficha9 Ex06
'''Faça um programa para gerir utilizadores/passwords.
O programa deve apresentar ao utilizador um menu com as seguintes opções:
a) Adicionar/Remover utilizador/password
b) Alterar password de um utilizador
c) Ver password de um utilizador
d) Ver lista completa de utilizadores/passwords.
Os pares utilizador/password devem constituir um dicionário.
Cada vez que o utilizador fizer login deve mostrar o tempo em que fez o último login
 (Deve usar o módulo do sistema time)'''

usr={}

while True:
    print("1 - Adicionar utilizador/password")
    print("2 - Remover utilizador/password")
    print("3 - Alterar password de um utilizador")
    print("4 - Ver password de um utilizador")
    print("5 - Ver lista completa de utilizadores/passwords.")
    print("0 - Sair")
    op=input("   Opção:")

    if op not in ('0','1','2','3','4','5'):
        print("     Opção inválida")

    elif op == '0':
        break

    elif op == '1': # add user
        u = input('\n Digite o Userid a adicionar: ')
        if u in usr.keys():
            print('   *** Userid já existente ***   ')
        else:
            pw = input(' Digite a password: ')
            usr[u]=pw

    elif op == '2': # Eliminar user
        u = input('\n Digite o Userid a eliminar: ')
        if u not in usr.keys():
            print('   *** Userid não existente ***   ')
        else:
            del(usr[u])

    elif op =='3': #Alterar password de um utilizador
        u = input('\n Alteração de Password - digite o Userid: ')
        if u not in usr.keys():
            print('   *** Userid não existente ***   ')
        else:
            pw = input(' Digite a nova password: ')
            usr[u] = pw

    elif op == '4': # Ver password de um utilizador
        u = input('\n Ver Password - digite o Userid: ')
        if u not in usr.keys():
            print('   *** Userid não existente ***   ')
        else:
            print(f' Password: {usr[u]}')

    elif op == '5': # Ver lista completa de utilizadores/passwords
        print(f'\n Lista de users passwords: \n    {usr}')
