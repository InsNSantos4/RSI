# Escreva uma função recursiva que permita calcular o fatorial de um número inteiro positivo pedido ao utilizador.

def fatorial(n):
    #caso base
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

inteiro = int(input("Introduza um inteiro positivo: "))

while inteiro < 0:
    inteiro = int(input("Introduza um inteiro positivo válido: "))
    
print(f"O fatorial de {inteiro} é {fatorial(inteiro)}.")