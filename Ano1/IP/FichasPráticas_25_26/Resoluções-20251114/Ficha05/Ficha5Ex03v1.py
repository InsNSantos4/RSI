#
# POP outubro 2023
#
# IP Ficha 05  Exercicio 03
#
# Números pares entre 1 e N
# Escreva um programa que apresente no ecrã os números pares entre 1 e N, sendo N um
# número inteiro positivo e fornecido pelo utilizador. Proceda à respetiva validação dos
# dados de entrada.

print("\n»»»»»»          Ficha 05  Exercicio 03")
print("\n»»»»»» ")
print("»»»»»»  Este programa apresenta no ecrã os números pares entre 1 e N, "
      "sendo N um número inteiro positivo")
print("»»»»»»\n ")
print("\n")

# Ler N com validação

while True:
    N = input("Entre valor de N: ")
    if Num.isnumeric():  # N é numerico
        N = int(N)
        if N > 0:  # N é maior que zero
            break #  sai do ciclo while
    print("»»»»»» N tem que ser um número inteiro positivo")

for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)

# fim do programa
