# Suponha que dispõe de uma cadeia de caracteres que contém uma frase cujas palavras
# estão separadas por um número arbitrário de espaços em branco.
# Escreva um programa que converta esta cadeia de caracteres numa nova cadeia de
# caracteres onde só exista um espaço em branco entre cada palavra.

string_1 = str(input("Introduza uma cadeia de caracteres: "))
print("\n")

cadeia_separada = string_1.split()

phrase = ''

for word in cadeia_separada:
    phrase = phrase + word + " "

print(phrase)