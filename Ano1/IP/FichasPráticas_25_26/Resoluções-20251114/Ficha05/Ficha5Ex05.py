# Ficha 5 Ex 05
# POP 2023

# Soma dos numeros naturais até N
print(" Este programa calcula a soma dos numeros naturais até N")

while True:
    N = int(input("Introduza o valor de N: "))
    if N > 0:
        break
    else:
        print("Valor de N inválido, N tem que ser um numero inteiro positivo")

soma = 0
for i in range(1,N+1):
    soma += i

print(f"A soma dos {N} primeiros numeros naturais é: {soma} ")

#fim do programa