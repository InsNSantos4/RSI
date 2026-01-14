# Ficha 6 Ex 06
# pop


# Faça um programa que peça ao utilizador dois valores inteiros e calcule a soma de todos
# os números pares entre eles, ambos inclusive.
# Exemplos:
# Valores introduzidos: 2 e 7 Resultado: 12
# Valores introduzidos: 5 e 10 Resultado: 24

print(" Este programa calcule a soma de todos os números pares entre 2 dois valores inteiros M e N, ambos inclusive.")

Valor1 = int(input(" Introduza o valor 1: "))
Valor2 = int(input(" Introduza o valor 2: "))


if Valor2 < Valor1:   # Valor1 tem que ser menor que Valor2. Csso seja maior, trocamos os valores.
    Valor1, Valor2 = Valor2,Valor1

soma_pares = 0
for numero in range(Valor1, Valor2+1):
    if numero % 2 == 0:
        soma_pares = soma_pares + numero

print(f" A soma dos números pares entre {Valor1} e {Valor2}  é {soma_pares}")

# fim
