#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 10
#
# Dígitos de um número
# a) Desenvolva um programa que, dado um número inteiro fornecido pelo utilizador,
# calcule o número de vezes que surge o algarismo zero nesse número.
# Exemplo: se o utilizador introduzir o número 3010, o programa deverá indicar que
# existem 2 zeros no número fornecido.
# b) Altere o programa anterior de modo a que este, para além de indicar quanto zeros
# existem no número, forneça também a indicação da posição dos mesmos.
# Exemplo: se o utilizador introduzir o número 3010, o programa deverá indicar que
# existem 2 zeros no número fornecido, nas posições 1 e 3.



print("\n»»»»»»          Ficha 05  Exercicio 10")
print("\n»»»»»» ")
print("»»»»»»  Este programa :")
print("»»»»»»      Dado um número inteiro fornecido pelo utilizador retorna o número de vezes que surge o algarismo zero nesse número")
print("»»»»»»      Retorna também a posição dos mesmos")
print("»»»»»»\n ")


# Ler N com validação

while True:
    Num = input("Entre o Numero: ")
    if Num.isdigit():  # N é numerico
        N = int(Num)
        if N >= 0:  # N é maior ou igual a zero
            break
    print("»»»»»» N tem que ser um número inteiro não negativo)")
print(N)
print()
# Alinea a) Contar zeros

# Usando  Strings (Forma 2) a resolução é muito mais simples

# Forma 1:
print("Forma 1: ")
# Podemos decompor o numero nos seus algarimos, tal como no exercicio 2 da ficha 4 (ISBN), testando cada algarismo
N_algarismos = 0 # Contador para o numero de algarismos de N
N_zeros = 0
Aux = N
P_zeros = ""
while Aux  > 0:
        N_algarismos += 1
        if Aux % 10 == 0:
            N_zeros += 1   # é o mesmo que N_zeros = N_zeros + 1
            P_zeros = P_zeros+" "+str(N_algarismos)
        Aux = Aux // 10

if N == 0:
    N_algarismos = 1
    N_zeros = 1
    P_zeros = "1"
if N_zeros == 0:
    P_zeros = "O numero não tem zeros"

print(f"Numero de algarismos: {N_algarismos}")
print(f"Numero de Zeros: {N_zeros}")
print(f"Posição dos zeros: {P_zeros}")

# Forma 2:

# Usando strings
print()
print("Forma 2  (usando strings): ")
Num = str(int(Num))   # Retira possiveis Zeros à esquerda
N_algarismos = len(Num)
N_zeros = Num.count("0")
print(f"Numero de algarismos: {N_algarismos}")
print(f"Numero de Zeros: {N_zeros}")

# Posição dos Zeros:
P_zeros = ""
if N_zeros > 0:
    for i in range(-1,-N_algarismos,-1):
        if Num[i] == "0":
            P_zeros = P_zeros+" "+str(-i)
if N == 0:
    P_zeros = "1"
if N_zeros == 0:
    P_zeros = "O numero não tem zeros"
print(f"Posição dos zeros: {P_zeros}")


# fim do programa
