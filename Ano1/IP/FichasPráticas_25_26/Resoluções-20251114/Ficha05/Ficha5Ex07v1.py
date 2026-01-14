#
# POP outubro 2023
#
# IP Ficha 05  Exercicio 07
#
# Números primos
# a) Escreva um programa que dado um número inteiro positivo N, fornecido pelo
# utilizador, verifique se o mesmo é ou não um número primo.
# Nota: Um número primo só é divisível por 1 e por si mesmo.
# b) Altere o programa de modo a que este permita apresentar no ecrã a lista de todos os
# números primos existentes entre 1 e 100.
# c) Modifique o programa para que imprima simplesmente os números primos gémeos,
# i.e., os números primos que diferem entre si de duas unidades (ex: 3 e 5, 11 e 13, ...).


print("\n»»»»»»          Ficha 05  Exercicio 07")
print("\n»»»»»» ")
print("»»»»»»  Este programa :")
print("»»»»»»      Verifica se um dado número inteiro positivo é ou não um número primo")
print("»»»»»»      Lista os Numeros Primos até 100")
print("»»»»»»      Lista os Numeros Primos Gémeos até 100")
print("»»»»»»\n ")
print("\n")

# Ler N com validação

while True:
    Num = input("Entre valor de N: ")
    if Num.isdigit():  # N é numerico
        N = int(Num)
        if N > 0:  # N é maior que zero
            N = int(N)
            break
    print("»»»»»» N tem que ser um número inteiro maior que zero)")

# Alinea a) Verifica se é primo

# Podemos testar se N é divisivel por outro numero (i)  de 1 até ele próprio
# mas o maior numero porque pode ser divisivel á a sua raiz quadrada
#  N = math.sqrt(N) * math.sqrt(N)
#  N  =  A * B    se A > math.sqrt(N)   ===>  B <  math.sqrt(N)
#    logo o se A é divisor de N e A é maior que a raiz quadrada de N, no calculo já tinhamos passado por B.
#    Por isso basta testar até à raiz quadrada do numero que estamos a validar
# https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-number-to-determine-if-the-number-is

RqN = N ** (0.5)  # raiz quadrada de N
finalRange = int(RqN + 1)
# finalRange = N
# se tiverem duvidas façam finalRange = N+1  :-)

for i in range(2, finalRange):
    if N % i == 0:  # se resto 0, é divisivel por i , logo não é primo
        print(f"{N} não é primo. É divisível por {i}")
        break
else:
    print(f"{N} é primo!")


print()

input('==> Prima "ENTER" para continuar <==')
print()
# Alinea b)

N = 100
print()

print(f"Numeros Primos até {N} :")

for j in range(1, N + 1):

    Rqj = j ** (0.5)  # raiz quadrada de j
    finalRange = int(Rqj + 1)
    for i in range(2, finalRange):
        if j % i == 0:
            break
    else:
        print(f"{j} ",end=" " )

print()

input('==> Prima "ENTER" para continuar <==')
print()
# Alinea c)
# primos gémeos


print()

print(f"Numeros Primos Gémeos até {N} :")

p1 = 0  # p1 vai ser usado para guardar o primo anterior

for j in range(1, N + 1):

    Rqj = j ** (0.5)  # raiz quadrada de j
    finalRange = int(Rqj + 1)
    for i in range(2, finalRange):
        if j % i == 0:
            break
    else:
        if j - p1 == 2:
            print(f"{p1}  {j} ")
        p1 = j
# fim do programa
