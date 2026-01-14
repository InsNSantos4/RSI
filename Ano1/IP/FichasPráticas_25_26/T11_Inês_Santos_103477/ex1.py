# Escreva uma função recursiva que calcule a soma dos primeiros n números naturais, sendo N introduzido pelo utilizador.

def soma_n(n):
    if n < 1:
        return 0
    return n + soma_n(n-1)

number = int(input("Introduza um número natural: "))

while number <= 0:
    number = int(input("Introduza um número natural (inteiro maior que zero): "))

print(f"A soma dos {number} primeiros números naturais é: {soma_n(number)}.")