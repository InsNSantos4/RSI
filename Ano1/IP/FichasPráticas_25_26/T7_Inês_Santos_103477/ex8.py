# Escreva um programa que calcule o número de letras maiúsculas de uma cadeira de
# caracteres.

string = input("Introduza uma string: ")

numberOf_uppers = 0
i = 0

while i < len(string):
    if string[i].isupper():
        numberOf_uppers += 1
    i = i + 1

print("Número de maiúsculas na string: " + str(numberOf_uppers))