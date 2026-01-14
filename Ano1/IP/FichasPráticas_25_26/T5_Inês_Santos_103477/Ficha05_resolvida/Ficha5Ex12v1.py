#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 12
#
# Pirâmide de números
# a) Implemente um programa que imprima no ecrã a seguinte pirâmide de números:
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# b) Altere o programa de modo a que o número de linhas da pirâmide seja fornecido
# pelo utilizador, efetuando a devida validação dos dados da entrada




print("\n»»»»»»          Ficha 05  Exercicio 12")
print("\n»»»»»» ")
print("»»»»»»  Pirâmide de Numeros")
print("»»»»»»  Este programa coloca no ecrã uma pirâmide de números.")
print("»»»»»»  O número de ramos N é introduzido pelo utilizador ")
print("»»»»»»\n ")
print("\n")

# Ler N com validação
while True:
    Num= input("Entre valor de N (1 a 9): ")
    if Num.isdigit():  # N é numerico
        N=int(Num)
        if 0<N<10  :  # N é maior que zero e menor que 10
            break
    print("»»»»»» N tem que ser um número inteiro  de 1 a 9")

# Forma 1
print()
print("Forma 1:")
for i in range (1,N+1):
    print((N-i) * " ",end="")
    for z in range(1, i + 1):
        print(z,end="")
    for j in range(i, 1, -1):
        print(j-1,end="")
    print()

# Forma 1A
print()

input('==> Prima "ENTER" para continuar <==')
print()
print("Forma 1A:")
for i in range (1,N+1):
    print((N-i) * "  ",end="")
    for j in range(1, i + 1):
        print(j,end=" ")
    for j in range(i, 1, -1):
        print(j-1,end=" ")
    print()

# Forma 2
input('==> Prima "ENTER" para continuar <==')
print()
print("Forma 2:")
for i in range (1,N+1):
    linha = (N-i) * " "
    for j in range(1, i + 1):
        linha = linha + str(j)
    for j in range(i, 1, -1):
        linha = linha + str(j-1)
    print(linha)

# Forma 3 (strings)
input('==> Prima "ENTER" para continuar <==')
print()
print("Forma 3:")
Ramo = Omar = ""
for i in range(1,N+1):
    Ramo = Ramo + str(i)      #12345
    Omar = Omar + str(N-i+1)  #54321

for i in range(1,N+1):
    linha = (N-i)*" " + Ramo[0:i] + Omar[N-i+1:N]
    print(linha)

# fim do programa
