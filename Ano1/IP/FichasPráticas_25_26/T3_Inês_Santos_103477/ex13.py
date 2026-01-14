# Classificação dos triângulos
# 13. Escreva um programa que classifique um triângulo quanto à dimensão dos lados:
# Escaleno - Todos os lados têm comprimentos diferentes
# Isósceles - Só dois lados com o mesmo comprimento
# Equilátero - Três lados com o mesmo comprimento.

print("Classificação de um triângulo...")

lado1 = float(input("Tamanho do lado 1 = "))
lado2 = float(input("Tamanho do lado 2 = "))
lado3 = float(input("Tamanho do lado 3 = "))

# Verifica primeiro se os lados introduzidos formam um triângulo válido
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if (lado1 == lado2 == lado3):
        print("É um triângulo equilátero.")
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Triângulo inválido.")
