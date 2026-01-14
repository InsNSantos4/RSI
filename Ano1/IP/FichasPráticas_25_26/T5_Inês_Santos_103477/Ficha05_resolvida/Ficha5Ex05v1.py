#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 05
#
# Soma dos números naturais
# Escreva um programa que calcule a soma dos N primeiros números naturais, sendo N
# fornecido pelo utilizador. Proceda à respetiva validação dos dados de entrada.
#
#   Número natural é definido como um número inteiro positivo,
#  não sendo o zero considerado como um número natural


print("\n»»»»»»          Ficha 05  Exercicio 05")
print("\n»»»»»» ")
print("»»»»»»  Este programa calcula a soma dos N primeiros números naturais, sendo N " \
      "fornecido pelo utilizador ")
print("»»»»»»  sendo N um número inteiro positivo")
print("»»»»»»\n ")
print("\n")

# Ler N com validação

while True:
    Num= input("Entre valor de N: ")
    if Num.isnumeric():  # N é numerico
        N=int(Num)
        if N > 0:  # N é maior que zero
            break
    print("»»»»»» N tem que ser um número Natural (inteiro maior que zero)")
soma = 0
for i in range (1,N+1):
    soma +=i

print(f"Soma dos {N} primeiros números naturais: ",soma)

# fim do programa
