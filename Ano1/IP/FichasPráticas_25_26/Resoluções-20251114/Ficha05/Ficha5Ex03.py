# Ficha 05 Exercicio 03
# POP 23

# Numeros pares entre um e N

print("Este programa retorna os numeros pares entre 1 e N sendo N inteiro positivo")
N = int(input("Introduza N: "))

for i in range(1,N+1):
    if i%2 == 0:
        print(i)

#fim do programa