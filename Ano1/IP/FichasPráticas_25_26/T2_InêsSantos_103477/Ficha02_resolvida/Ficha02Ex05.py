#
# POP Setembro 2023
#
# IP Ficha 02  Exercicio 05
#
# 	Com base na resolução anterior escreva um programa que para alem de identificar
# 	se um número é positivo ou negativo identifique também se o número é igual a zero.

# Ler número
Numero = float(input("Entre um número : "))

# Verificar se número é positivo
Positivo = (Numero > 0)

# Verificar se número é negativo
Negativo = (Numero < 0)

# Verificar se número é igual a zero
Zero = (Numero == 0)


# Forma 1
print('** Forma 1: ')
#  diga se o número é positivo ou negativo.
print('o numero é positivo: ', Positivo)
#  diga se o número é negativo.
print('o numero é negativo: ', Negativo)
#  diga se o número é igual a Zero.
print('o numero é igual a Zero: ', Zero)
print()

# Forma 2
print('** Forma 2: ')
print('o numero é positivo! '*Positivo)
print('o numero é negativo! '*Negativo)
print('o numero é igual a Zero! '*Zero)
print()

# Forma 3
print('** Forma 3: ')
print('o numero é positivo! '*Positivo + 'o numero é negativo! '*Negativo +'o numero é igual a Zero! '*Zero)
print()