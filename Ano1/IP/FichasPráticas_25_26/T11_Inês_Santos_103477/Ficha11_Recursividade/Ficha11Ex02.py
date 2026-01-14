# Ficha 11 Ex02


'''Escreva uma função recursiva que permita calcular
a soma de todos os dígitos de um número inteiro
positivo inserido pelo utilizador.'''

def soma_dig(N):
    if N ==0:
        return 0
    if N > 0:
        # print(N, ' + ', end='')
        dig = N % 10
        novo_num = N//10
        resultado = dig + soma_dig(novo_num)
        return resultado
    else:
        return 'Inserido Valor Inválido'

numero = int(input('Calculo da soma dos algarismos de um numero:\nEntre o valor de N: '))
print('\nSoma :',soma_dig(numero))