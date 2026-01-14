#
# POP Setembro 2022
#
# IP Ficha 02  Exercicio 07
#
# 	Escreva um programa que identifique se um número é ímpar ou par..

#  "par é o todo número que pode ser escrito na forma 2*n", com pertencente ao conjunto dos números inteiros.

# Ler o Numero
Numero = int(input("Entre um numero inteiro:") )
# print(Numero)

# Se é par é divisivel por 2 => resto da divisão = 0
# Se é impar não é divisivel por 2 => resto da divisão = 1
Resto = Numero%2

# resto da divisão = 0 é par

Par = (Resto==0)
# se é par então PAR fica com o valor TRUE. Se é impar fica com o valor False

# resto da divisão = 1 é impar
Impar = (Resto==1)
# se é impar então IMPAR fica com o valor TRUE. Se é par fica com o valor False


# Retornar o resultado
print('O numero',Numero, 'é impar'*Impar + 'é par'*Par)




