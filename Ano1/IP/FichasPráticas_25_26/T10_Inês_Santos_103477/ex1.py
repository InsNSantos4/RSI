# Escreva uma função que recebe por parâmetro o raio de uma esfera e calcula o seu
# volume (V = 4/3 * π * r3). Utilize a função num programa para calcular o volume de uma
# esfera cujo valor do raio é fornecido pelo utilizador do programa. O raio deve ser sempre
# um valor real maior ou igual a zero.

import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius**3)

raio = float(input("Introduza o valor do raio de uma esfera: "))
raio_valido = False

while raio_valido == False:
    if raio >= 0:
        raio_valido = True
        print(f'O volume da esfera com raio {raio} é: {sphere_volume(raio):.2f}')
    else:
        print("Erro: Valor de raio inválido (tem que ser real >= 0).")
        raio = float(input("Introduza o valor do raio de uma esfera: "))
    print("\n")