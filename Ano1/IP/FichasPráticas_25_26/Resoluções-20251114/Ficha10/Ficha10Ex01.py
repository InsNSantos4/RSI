# Ficha 10 Ex01
'''Escreva uma função que recebe por parâmetro o raio de uma esfera
e calcula o seu volume (V = 4/3 * π * r3). Utilize a função num
programa para calcular o volume de uma esfera cujo valor do raio
é fornecido pelo utilizador do programa. O raio deve ser sempre
um valor real maior ou igual a zero.'''

import math

def vol_esfera(raio):
    v = 4/3 * math.pi * raio**3
    return v

r = float(input(' Calculo do Volume de uma esfera. \n Introduza o valor do raio:'))
volume = vol_esfera(r)

print(f'Volume da esfera: {volume}')
