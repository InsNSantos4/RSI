#
# POP Setembro 2023
#
# IP Ficha 02  Exercicio 04
#
# 	Escreva um programa que leia um número inteiro diferente de zero
# 	e diga se o número é positivo ou negativo.

# Ler número inteiro diferente de zero
Numero = int(input("Entre um número inteiro diferente de zero: "))

# Verificar se número é positivo
Positivo = (Numero > 0)
# Se é positivo ( maior que zero) então a variavel Positivo fica com o valor TRUE.
#  Se não é, fica como valor False

# Verificar se número é negativo
Negativo = (Numero < 0)
# Se é negativo ( menor que zero) então a variavel Negativo fica com o valor TRUE.
#  Se não é, fica como valor False


# Forma 1
print('** Forma 1: ')
#  diga se o número é positivo ou negativo.
print('o numero é positivo: ', Positivo)
#  diga se o número é negativo.
print('o numero é negativo: ', Negativo)
print()

# Forma 2
print('** Forma 2: ')
R1 = 'o numero é positivo! '*Positivo
print(R1)
# ou:   print('o numero é positivo! '*Positivo)  #
R2 = 'o numero é negativo! '*Negativo
print(R2)
# ou: print('o numero é negativo! '*Negativo)
print()



# Forma 3
print('** Forma 3: ')

print('o numero é positivo! '*Positivo + 'o numero é negativo! '*Negativo)
print()


# Forma 4
# usando as variaveis R1 e R2 definidas na forma
print('** Forma 4: ')
print(R1+R2)
