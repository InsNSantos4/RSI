#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 04
#
# 4. Múltiplos de 3 entre m e M
# Implemente um programa que imprima no ecrã os múltiplos de 3 entre m e M, sendo m
# e M fornecidos pelo utilizador e em que m tem de ser inferior a M. Proceda à respetiva
# validação dos dados de entrada.

print("\n»»»»»»          Ficha 05  Exercicio 04")
print("\n»»»»»» ")
print("»»»»»»  Este programa imprime no ecrã os múltiplos de 3 entre m e M")
print("»»»»»»  m e M fornecidos pelo utilizador e m tem de ser inferior a M")
print("»»»»»»\n ")
print("\n")

while True:
    m1 = input("Entre valor de m: ")
    if m1.isnumeric():  # m é numerico
        m = int(m1)
        break
    print("»»»»»» m tem que ser um número inteiro positivo")

while True:
    M1 = input("Entre valor de M (deve ser maior que " + m1 + "): ")
    if M1.isnumeric():  # M é numerico
        M = int(M1)
        if M > m:
            break
    print("»»»»»» M tem que ser um número inteiro maior que " + m1)

print()
Multiplo = False
for i in range(m, M + 1):
    if i % 3 == 0:
        print(i, end=" ")
        Multiplo = True

if Multiplo == False:
    print()
    print(f"   Não há multiplos de 3 no intervalo de {m} a {M}")

# fim do programa
