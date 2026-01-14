# Escreva um programa capaz de ler uma matriz M 5x5 
# e calcular o maior elemento de cada linha da matriz 
# e a média dos elementos de cada coluna.

# Ler matriz 5x5:
n = 5
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(n):
        element = float(input(f"Introduza o elemento[{i+1}][{j+1}] da matriz M 5x5 (elemento tem que ser um número) -> "))
        matriz[i].append(element)

print("\n")

# Cálculo do maior elemento de cada linha:
for i in range(0,5):
        print(f"O maior elemento da linha {i+1} é {max(matriz[i])}.")

print()

# Cálculo da média dos elementos de cada coluna da matriz:
for j in range(n):
    sum_column = 0     # assim a soma é renovada a cada nova coluna
    for i in range(n):
        sum_column += matriz[i][j]
    print(f"A média dos elementos da coluna {j+1} é {(sum_column/n):.1f}.")
    print("\n")