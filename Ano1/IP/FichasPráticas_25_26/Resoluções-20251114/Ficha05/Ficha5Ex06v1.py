#
# POP outubro 2023
#
# IP Ficha 05  Exercicio 06
#
# 6. Fatorial
# a) Escreva um programa que permita calcular o fatorial de um número N inteiro positivo,
# fornecido pelo utilizador. Proceda à respetiva validação dos dados de entrada.
# b) Altere o programa de modo que este permita calcular o fatorial de todos os números
# entre 1 e N, sendo N um número inteiro positivo fornecido pelo utilizador.
# Exemplo da saída de dados:
# O fatorial de 1 é 1
# O fatorial de 2 é 2
# O fatorial de 3 é 6

# NOTA:  Nesta resolução considerei também o valor "0" apesar de não ser pedido no enunciado


print("\n»»»»»»          Ficha 05  Exercicio 06")
print("\n»»»»»» ")
print('»»»»»»  Este programa calcula o fatorial de um número N inteiro positivo (N!)')
print('»»»»»»    NOTA:  Nesta resolução considerei também o valor "0" apesar de não ser pedido no enunciado\n')
print("\n")

# Ler N com validação

while True:
    Num = input("Entre valor de N: ")
    if Num.isnumeric():  # N é numerico
        N = int(Num)
        if N >= 0:  # N é maior ou igual a zero
            break
    print("»»»»»» N tem que ser um número inteiro positivo)")
print()
print('Forma 1:  ')
# Alinea a)
fact = 1
for i in range(1, N + 1):
    fact *= i

print(f"O factorial de {N} ({N}!) é: {fact}")

# Alinea b)
print(f"O factorial dos numeros de 0 a {N} :")

for j in range(0, N + 1):
    fact = 1
    for i in range(1, j + 1):
        fact *= i  # é o mesmo que:   fact = fact * i
    print(f"{j:5}! = {fact}")

# Forma 2  - Usando função

print()

input('==> Prima "ENTER" para continuar <==')
print()

print('Forma 2  - definindo (criando) função:')
def fatorial(x):
    if x != 0:
        f = x*fatorial(x-1)
    else:
        f = 1
    return f


# Alinea a)
fact = fatorial(N)
print(f"O factorial de {N} ({N}!) é: {fact}")

# Alinea b)
print(f"O factorial dos numeros de 0 a {N} :")
for j in range(0,N+1):
    print(f"{j}! : ",fatorial(j) )
# fim do programa
