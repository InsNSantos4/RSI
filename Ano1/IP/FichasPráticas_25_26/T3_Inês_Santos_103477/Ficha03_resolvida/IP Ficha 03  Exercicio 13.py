#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 13
#
# Classificação dos triângulos
# 13. Escreva um programa que classifique um triângulo quanto à dimensão dos lados:
#   Escaleno - Todos os lados têm comprimentos diferentes
#   Isósceles - Só dois lados com o mesmo comprimento
#   Equilátero - Três lados com o mesmo comprimento.

print("\n»»»»»» ")
print("»»»»»»  Este programa classifica um triângulo quanto à dimensão dos seus lados")
print("»»»»»»\n ")
print("\n")

# Ler 1º lado
l_1 = float(input("Entre valor do 1º lado do triângulo : "))

# Ler 2º lado
l_2 = float(input("Entre valor do 2º lado do triângulo : "))

# Ler 3º lado
l_3 = float(input("Entre valor do 3º lado do triângulo : "))

# Validação
if l_1 == l_2 == l_3:  # ou  (L1 == L2) and (L1 == L3)
    # Lados iguais
    print(" O triângulo é EQUILÁTERO - Os três lados têm o mesmo comprimento ")

elif (l_1 != l_2) and (l_1 != l_3) and (l_2 != l_3):
    # Lados todos diferentes
    print(" O triângulo é ESCALENO - Todos os lados têm comprimentos diferentes")

else:
    # 2 Lados iguais e um diferente
    print(" O triângulo é ISÓSCELES - Só dois lados têm o mesmo comprimento ")

# fim do programa