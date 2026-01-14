# Ficha 10 Ex03
'''Desenvolva uma função que permita calcular o índice de
massa corporal (IMC) de um dado indivíduo. A função deve aceitar 
como parâmetros a altura (em metros) e o peso (em kg).
Protótipo da função: def imc(altura, peso)
NOTA: IMC = massa / altura2
Implemente outra função que permita obter a classificação da 
situação do individuo de acordo com a tabela seguinte:'''


def imc(altura, peso):
    indice = peso/(altura**2)
    return indice

def situacao(i):
    if i < 18.5:
        msg='Abaixo do peso ideal'
    elif i < 25:
        msg='Peso ideal'
    elif i < 30:
        msg='Acima do peso ideal'
    else:
        msg='Obeso'
    return msg

while True:
    print()
    print('*****************')
    print('Menu:')
    print('1. Calcular IMC')
    print('2. Sair')
    print('*****************')
    opcao = input('Opção: ')
    if opcao == '2':
        print('Fim!')
        break
    elif opcao == '1':
        p =float(input('Introduza o peso: '))
        a =float(input('Introduza a altura: '))
        #invocar função imc()
        ind_massa_corporal= imc(a,p)
        print(f'IMC: {ind_massa_corporal:.1f}')
        #invocar função situação()
        sit_imc = situacao(ind_massa_corporal)
        print('Situação: ',sit_imc)
    else:
        print('>>> Opção Inválida <<<\n')

# Fim