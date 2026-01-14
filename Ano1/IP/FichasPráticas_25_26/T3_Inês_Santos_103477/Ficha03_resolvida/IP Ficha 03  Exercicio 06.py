#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 06
#
#  Par ou ímpar
# 6. Escreva um programa que dado um número inteiro introduzido pelo utilizador indique se
#    o número é, ou não, par.

#  "um número é par quando ser escrito na forma 2*n", com pertencente ao conjunto dos números inteiros.

print("\n»»»»»» ")
print("»»»»»»  Este programa determina se um número inteiro é, ou não, par")
print("»»»»»»\n ")

# Ler o Numero
numero_input = input("Entre um número inteiro: ")
numero = int(numero_input)
# print(numero)

# Se é par é divisivel por 2 => resto da divisão = 0
# Se é impar não é divisivel por 2 => resto da divisão = 1
valida_par = (numero % 2 == 0)
if valida_par:
    print('O número',numero,'é par')
else:
    print('O número',numero,'é impar')



# fim do programa

