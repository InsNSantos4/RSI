# Ficha 11 Ex04

'''Escreva uma função recursiva que aceite um inteiro decimal e exiba
 o seu equivalente em binário.'''

def conv_bin(n):
    b = ""
    if n > 0:
        b = conv_bin(n // 2) + str(n % 2)
    return b


numero = int(input('Conversão de numero N, base 10 para binário:\nEntre o valor de N: '))
print('\nBinãrio :',conv_bin(numero))