#
# POP outubro 2022
#
# IP Ficha 04  Exercicio 02
#
# Número ISBN
# 2.	O código ISBN de um livro é uma "sequência" de 10 algarismos.
# Os primeiros algarismos identificam a língua em que foi escrito
# ou o país onde foi publicado, conforme os casos. Os algarismos seguintes
# a editora e o livro, e o último é um algarismo de controlo, tal como nos casos dos códigos de barras.
# Um número x10x9x8 − x7x6x5 − x4x3x2 − x1 é um número ISBN se verifica a seguinte regra:
# x1 + 2∗x2 + 3∗x3 + 4∗x4 + 5∗x5 + 6∗x6 + 7∗x7 + 8∗x8 + 9∗x9 + 10∗x10 é múltiplo de 11 ou é divisível por 11.
# O dígito de controlo é x1.
# Elabore um programa que permita receber uma sequência de 10 algarismos verificando
# se a mesma pode ser considerada como um código ISBN de um livro.
#  972-662-905-5 	Portugal 	Gradiva      9726629055
#  85-359-0277-5 	Brasil 	Companhia das Letras  8535902775
#  0-684-84328-5 	English-speaking area 	Scribner  0684843285
#  0-85131-041-9 	English-speaking area 	J. A. Allen & Co.  0851310419
#  0-943396-04-2 	English-speaking area 	Willmann–Bell      0943396042



print("\n»»»»»» ")
print("»»»»»»  Este programa lê ouma sequência de 10 algarismos verificando ")
print("»»»»»»  se a mesma pode ser considerada um código ISBN de um livro.")
print("»»»»»»\n ")
print("\n")

# Ler ISBN
isbn = int(input("Entre valor do ISBN (10 digitos): "))

x1 = isbn % 10  # obter 1º digito  ex: 2348 -> 8
aux = isbn // 10 # obter o numero  sem o 1º digito  ex: 2348 -> 234

x2 = aux % 10  # obter 2º digito ex:   234 -> 4
aux = aux // 10  # obter o numero  sem o 2º digito  ex: 234 -> 23

x3 = aux % 10   # obter 3º digito ex:   23 -> 3
aux = aux // 10   # obter o numero  sem o 3º digito  ex: 23 -> 2

x4 = aux % 10
aux = aux // 10

x5 = aux % 10
aux = aux // 10

x6 = aux % 10
aux = aux // 10

x7 = aux % 10
aux = aux // 10

x8 = aux % 10
aux = aux // 10

x9 = aux % 10
aux = aux // 10

x10 = aux % 10

print('Valor a validar como ISBN:', str(x10)+str(x9)+str(x8), '-',
      str(x7)+str(x6)+str(x5), '-', str(x4)+str(x3)+str(x2), '-',str(x1))

calculo = x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9 + 10*x10

if calculo % 11 == 0:
    print('   »»»  A sequência inserida é um ISBN válido.')
else:
    print('   »»»  A sequência inserida não é um ISBN válido.')

# fim do programa
