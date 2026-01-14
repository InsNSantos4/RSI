'''Escreva uma função recursiva que calcule a soma dos numeros pares nos primeiros n números naturais,
 sendo N introduzido pelo utilizador.'''

def somap(N):
    if N ==0:
        # print(1)
        return 0
    if N > 0:
        # print(N, ' + ', end='')
        if N % 2 == 0:
            resultado = N + somap(N-1)
        else:
            resultado =  somap(N-1)
        return resultado


numero = int(input('Calculo da soma dos N primeiros numeros naturais \nEntre o valor de N: '))
print('\nSoma :',somap(numero))
