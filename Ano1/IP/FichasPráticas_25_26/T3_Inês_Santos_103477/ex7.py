# Raiz quadrada de um número inteiro
# 7. Escreva um programa que leia um valor inteiro e que 
# indique a respetiva raiz quadrada.

import math

num_int = int(input("Please write an integer number: "))
print('\n')

# 2 métodos para calcular a raiz de um número:
print(math.sqrt(num_int))
print((num_int)** 0.5)