# Ficha 11 Ex02


'''Escreva uma função recursiva que permita calcular
a soma de todos os dígitos de um número inteiro
positivo inserido pelo utilizador.'''

def soma_dig(N):
    if len(N) == 0:
        return 0
    if len(N) > 0:
        # print(N, ' + ', end='')
        dig = N[-1]
        novo_num = N[:-1]
        resultado = int(dig) + soma_dig(novo_num)
        return resultado
    else:
        return 'Inserido Valor Inválido'

numero = input('Calculo da soma dos algarismos de um numero:\nEntre o valor de N: ') # mantem como string
print('\nSoma :',soma_dig(numero))