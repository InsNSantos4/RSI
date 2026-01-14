# Ficha 11 Ex01

#

'''Escreva uma função recursiva que calcule a soma dos primeiros n números naturais,
 sendo N introduzido pelo utilizador.'''

def soma(numero):
    if numero ==1:
        #print(1)
        return 1
    if numero > 0:
        # print(N, ' + ', end='')
        resultado = numero + soma(numero-1)
        print('Nº Execução: ',numero)
        return resultado
    else:
        return 'Inserido Valor Inválido'

numero = int(input('Calculo da soma dos N primeiros numeros naturais \nEntre o valor de N: '))
print('\nSoma :',soma(numero))
