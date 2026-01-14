#
# POP outubro 2023
#
# IP Ficha 04  Exercicio 01
#
# Raízes de Polinómios
# 1.	Escreva um programa que leia do teclado os coeficientes
# de uma equação de 2º grau (Ax2 + Bx + C = 0),
# que a resolva e que indique o valor das raízes associadas, da seguinte forma:
# Duas raízes reais diferentes: xxx.xxx e xxx.xxx
# Ou
# Duas raízes reais iguais: xxx.xxx

print("\n»»»»»» ")
print("»»»»»»  Este programa lê os coeficientes de uma equação de 2º grau (Ax**2 + Bx + C = 0)")
print("»»»»»»  e determina o valor das raízes associadas")
print("»»»»»»\n ")
print("\n")

# Ler coeficiente A
a = float(input("Entre valor do coeficiente A : "))

# Ler coeficiente B
b = float(input("Entre valor do coeficiente B : "))

# Ler coeficiente C
c = float(input("Entre valor do coeficiente C : "))

# raizes de uma equacação do 2º grau:
#  1ª raiz:   (-B + (B**2 - 4*A*C)**0.5 ) / 2*A
#  2ª raiz:   (-B - (B**2 - 4*A*C)**0.5 ) / 2*A    # 3 6 3    2 8 8

raiz_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
raiz_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(' As raizes da equação são:')
if raiz_1 != raiz_2:
    print('     Duas raízes reais diferentes:', raiz_1, 'e', raiz_2)
else:
    print('    Duas raízes reais iguais:', raiz_1)

# fim do programa
# -2 1 1 -> 0.5 e 1
# 2 2 -4 -> 1 e -2
