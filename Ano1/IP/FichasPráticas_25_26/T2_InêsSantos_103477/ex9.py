# Programa que para além de identificar se um número é positivo ou negativo identifique também se o número é igual a zero:

print("Introduza um número inteiro diferente de zero: ")

num = float(input())

if num == 0:
    print("O número que introduziu foi o zero.")
if num > 0:
    print("Número positivo.")
else:
    print("Número negativo.")