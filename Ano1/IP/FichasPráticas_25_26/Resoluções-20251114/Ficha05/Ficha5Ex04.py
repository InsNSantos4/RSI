# Ficha 5 Ex 04
# POP 2023
# Multiplos de 3 entre m e M

print("Calculo dos multiplos de entre m e M")

N = int(input("Introduza o valor de m: "))
M = int(input("Introduza o valor de M (tem que ser maior que m): "))

if M <= N:
    print("\n===> Valores inválidos: M tem que ser maior que m ")
else:
    for i in range (m,M+1):
        if i % 3  == 0:
            print(i) #  print(i, end=" ")
