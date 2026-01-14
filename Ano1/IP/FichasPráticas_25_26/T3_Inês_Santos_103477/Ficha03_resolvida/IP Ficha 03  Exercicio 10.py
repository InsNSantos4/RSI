#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 10
#
# Maior de dois números
# 10. Escreva um programa que leia dois números e indique o maior deles. O programa deverá
# contemplar a situação dos dois números serem iguais.

print("\n»»»»»» ")
print("»»»»»»  Este programa lê dois números e indica qual o maior deles")
print("»»»»»»\n ")

# Ler 1º número
num_1 = int(input("Entre o 1º número : "))

# Ler 2º número
num_2 = int(input("Entre o 2º número : "))

if (num_1 > num_2):
    print('O número maior é o 1º número: ' + str(num_1))

elif (num_2 > num_1):
    print('O número maior é o 2º número: ' + str(num_2))

else:
    print('O 1º e o 2º números são iguais: ' + str(num_1))

# fim do programa
