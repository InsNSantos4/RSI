#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 11
#
# Pirâmide de Asteriscos
# Escreva um programa que coloque no ecrã meia árvore de Natal com asteriscos. O
# número de ramos deverá ser introduzido pelo utilizador.
# Exemplos com 3, 4 e 5 ramos:
# *                 *                *
# **                **               **
# ***               ***              ***
#                   ****             ****
#                                    *****



print("\n»»»»»»          Ficha 05  Exercicio 11")
print("\n»»»»»» ")
print("»»»»»»  Pirâmide de Asteriscos")
print("»»»»»»  Este programa coloca no ecrã meia árvore de Natal com asteriscos.")
print("»»»»»»  O número de ramos N é introduzido pelo utilizador ")
print("»»»»»»\n ")
print("\n")

# Ler N com validação

while True:
    Num= input("Entre valor de N: ")
    if Num.isdigit():  # N é numerico
        N=int(Num)
        break
    print("»»»»»» N tem que ser um número inteiro")


# Forma 1
print("Forma 1:")
for i in range (1,N+1):
    print(i * "*") # + (i - 1) * " ")

# Forma 2
print()
input('==> Prima "ENTER" para continuar <==')
print()

print("Forma 2")
for i in range (1,N+1):
    for j in range(1,i+1):
       print("*",end="")
    print()

# Forma 3
print()
input('==> Prima "ENTER" para continuar <==')

print()
print("Forma 3")
Ramo = N * "*"
for i in range(1,N+1):
    print(Ramo[0:i])








# fim do programa
