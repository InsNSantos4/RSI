# Ficha 11 Ex03

'''Escreva uma função recursiva que permita calcular o fatorial
de um número inteiro positivo pedido ao utilizador.'''

def fatorial(N):
    if N ==0:
        return 1
    if N > 0:
        # print(N, ' + ', end='')
        resultado = N  * fatorial(N-1)
        return resultado

numero = int(input('Calculo do Fatorial (N!) de um numero:\nEntre o valor de N: '))
print('\nFatorial :',fatorial(numero))

3*2*1
2*1
1
1