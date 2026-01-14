#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 08
#
# Máximo divisor comum
# Implemente um programa que permita calcular o máximo divisor comum – mdc(m,n) –
# entre dois números inteiros positivos m e n fornecidos pelo utilizador. Proceda à
# respetiva validação dos dados de entrada.

print("\n»»»»»»          Ficha 05  Exercicio 08")
print("\n»»»»»» ")
print("»»»»»»  Este programa permite calcular o máximo divisor comum – mdc(m,n)")
print("»»»»»»  entre dois números inteiros positivos m e n ")
print("»»»»»»\n ")
print("\n")

while True:
    m1 = input("Entre valor de m: ")
    if m1.isdigit():  # m é numerico
        m = int(m1)
        if m > 0 :  # m é maior que zero
            break
    print("»»»»»» m tem que ser um número inteiro positivo")

while True:
    n1 = input("Entre valor de n: ")
    if n1.isdigit():  # n  é numerico
        n = int(n1)
        if n > 0 :  # n é maior que 0
            n = int(n)
            break
    print("»»»»»» tem que ser um número inteiro positivo")

if m > n:
    maior = m
    menor = n
else:
    maior = n
    menor = m


print("\n\n»»»»»» Cálculo pelo método tradicional:")
# Condição
i = 1
while i <= menor:
    if menor % i == 0 and maior % i == 0:
        # print(i,"é divisor de",maior,"e",menor )
        a = i
        i = i + 1
        continue
    else:
        i = i + 1
print(f"   MDC({maior},{menor}) = {a}")
print()

print("\n\n»»»»»» Cálculo pelo Algoritmo de Euclides:")

A1 = maior
B1 = menor

MDC = 1

while True:
    Resto = A1 % B1
    if Resto == 0:
        break
    else:
         A1 = B1
         B1 = Resto

print(f"   MDC({maior},{menor}) = {B1}")


# fim do programa
