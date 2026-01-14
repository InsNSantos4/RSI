#
# POP Setembro 2023
#
# IP Ficha 02  Exercicio 02
#
# Escreva um programa que calcule a área de um retângulo.

# Lado1
Lado1 = input('Tamanho lado 1: ')  # Ler do teclado Lado1  -> fica tipo string
print(type(Lado1))
Lado1A = int(Lado1)  # Converter a variavel Lado1 para inteiro
print(type(Lado1A))

# Lado2
#Lado2 = input('Tamanho Lado2: ')  # Ler do teclado Lado2  -> fica tipo string
# print(type(Lado2))
Lado2 = int(input('Tamanho Lado2: '))  # Converter a variavel Lado2 para inteiro
# print(type(Lado2))

#calculoo da area
Area = Lado1A * Lado2   # Cálculo da área
print(' Área do rectângulo: ', Area)   # Print da área
