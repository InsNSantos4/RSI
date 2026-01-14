# Escreva uma função recursiva que calcule a soma dos primeiros n números naturais, sendo N introduzido pelo utilizador.

def soma_n(n):
    if n < 1:
        return 0
    return n + soma_n(n-1)

# Escreva uma função recursiva que permita calcular a soma de todos os dígitos de um número inteiro positivo inserido pelo utilizador.

def sum_digits(num):
    digits = str(num)
    #caso base
    if len(digits) == 1:
        return int(digits)
    #otherwise:
    return int(digits[0]) + sum_digits(digits[1:])


# Escreva uma função recursiva que permita calcular o fatorial de um número inteiro positivo pedido ao utilizador.

def fatorial(n):
    #caso base
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


# Escreva uma função recursiva que aceite um inteiro decimal e exiba o seu equivalente em binário.

def decimal_to_binary(decimal_num):
    #caso base:
    if decimal_num == 0 or decimal_num == 1:
        return str(decimal_num)
    else:
        # binário da parte inteira da divisão por 2 + resto da divisão por 2
        return decimal_to_binary(decimal_num // 2) + str(decimal_num % 2)