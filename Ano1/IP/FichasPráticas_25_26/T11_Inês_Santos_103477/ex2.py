# Escreva uma função recursiva que permita calcular a soma de todos os dígitos de um número inteiro positivo inserido pelo utilizador.

def sum_digits(num):
    digits = str(num)
    #caso base
    if len(digits) == 1:
        return int(digits)
    #otherwise:
    return int(digits[0]) + sum_digits(digits[1:])


inteiro = int(input("Introduza um inteiro positivo: "))

while inteiro < 0:
    inteiro = int(input("Introduza um inteiro positivo válido: "))

print(f"A soma dos dígitos do número que inseriu ({inteiro}) é {sum_digits(inteiro)}.")