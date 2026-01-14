#  Programa que leia um número inteiro diferente de zero e diga se o número é positivo ou negativo

print("Introduza um numero inteiro diferente de zero: ")

num = int(input())

if num != 0:
    if num > 0:
        print("Número positivo.")
    else:
        print("Número negativo.")