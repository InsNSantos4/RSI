# Ficha 11 Ex Novo


'''Escreva uma função recursiva que permita calcular
a soma de todos os dígitos pares de um número inteiro
positivo inserido pelo utilizador.'''

def soma_dig(N):
    if N ==0:
        return 0
    if N > 0:
        # print(N, ' + ', end='')
        dig = N % 10
        novo_num = N//10
        if dig % 2 == 0:
            resultado = dig + soma_dig(novo_num)
        else:
            resultado = soma_dig(novo_num)

        return resultado

numero = int(input('Calculo da soma dos algarismos pares de um numero:\nEntre o valor de N: '))
print('\nSoma :',soma_dig(numero))