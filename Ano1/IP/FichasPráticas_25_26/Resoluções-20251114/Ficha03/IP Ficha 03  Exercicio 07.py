#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 07
#
#  Raiz quadrada de um número inteiro
# 7. Escreva um programa que leia um valor inteiro e que indique a respetiva raiz quadrada.

print("\n»»»»»» ")
print("»»»»»»  Este programa lê um valor inteiro e calcula a respetiva raiz quadrada")
print("»»»»»»\n ")

# Ler o Numero
numero = int(input("Entre um número inteiro: "))
# print(numero)

# calculo da raiz quadrada
raizQ = numero ** (1/2)
print('A raiz quadrada de', numero, "é", raizQ)
# ou
import math
raizQ1= math.sqrt(numero)
print(f'A raiz quadrada de {numero} é {raizQ1} ')


# fim do programa