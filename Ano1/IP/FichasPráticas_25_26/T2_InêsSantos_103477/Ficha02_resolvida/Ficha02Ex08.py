# _*_ coding: utf-8 _*
#
# POP Setembro 2022
#
# IP Ficha 02  Exercicio 08
#
# 	Escreva um programa que receba 3 números e devolva qual o maior.

# Ler 1º número
Num_1 = int(input("Entre o 1º número : "))

# Ler 2º número
Num_2 = int(input("Entre o 2º número : "))

# Ler 3º número
Num_3 = int(input("Entre o 3º número : "))

M1 = (Num_1 > Num_2) and (Num_1 > Num_3)  # True se Num_1 for o maior
M2 = (Num_2 > Num_1) and (Num_2 > Num_3)  # True se Num_2 for o maior
M3 = (Num_3 > Num_2) and (Num_3 > Num_1)  # True se Num_3 for o maior

print('O numero maior é o: ' + str(Num_1) * M1 + str(Num_2) * M2 + str(Num_3) * M3)
print()

M1 = (Num_1 >= Num_2) and (Num_1 > Num_3)  # True se Num_1 for o maior
M2 = (Num_2 > Num_1) and (Num_2 >= Num_3)  # True se Num_2 for o maior
M3 = (Num_3 > Num_2) and (Num_3 >= Num_1)  # True se Num_3 for o maior

print('O numero maior é o: ' + str(Num_1) * M1 + str(Num_2) * M2 + str(Num_3) * M3)
print()

M1 = (Num_1 >= Num_2) and (Num_1 > Num_3)  # True se Num_1 for o maior
M2 = (Num_2 > Num_1) and (Num_2 >= Num_3)  # True se Num_2 for o maior
M3 = (Num_3 > Num_2) and (Num_3 >= Num_1)  # True se Num_3 for o maior

# Se forem os 3 iguais
M4 = (Num_1 == Num_2) and (Num_1 == Num_3)
# M4 = ( Num_1 == Num_2 == Num_3 )
# M4=  not (M1 or M2 or M3)
print('O numero maior é o: ' + str(Num_1) * M1 + str(Num_2) * M2 + str(Num_3) * M3 + str(Num_1) * M4)
print()
