# Ficha 5 Ex 06a
# POP 2023

# Calculo do factorial de N
print(" Este programa calcula o factorial do nº N")

while True:
    N = int(input("Introduza o valor de N: "))
    if N > 0:
        break
    else:
        print("Valor de N inválido, N tem que ser um numero inteiro positivo")

fact = 1
for i in range(1,N+1):
    fact = fact*i

print(f"O factorial de N ( N! ): {fact} ")