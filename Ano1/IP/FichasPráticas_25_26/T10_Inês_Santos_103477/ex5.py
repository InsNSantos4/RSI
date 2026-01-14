# Escreva uma função que receba, por parâmetro, uma matriz A quadrada e a sua
# dimensão, multiplicando a soma de todos os elementos de cada linha pelo elemento da
# diagonal principal da própria linha.
# A função deve retornar a soma de todos os valores calculados.
# Implemente um programa que permita testar a função desenvolvida.

def mult_lineElemsByDiagonalElems(matriz_quadrada, dimension):
    total_sum = 0
    
    for i in range(dimension):
        sum_line = 0
        sum_line_multiplied = 0
        for j in range(dimension):
            sum_line += matriz_quadrada[i][j]
        sum_line_multiplied = sum_line * matriz_quadrada[i][i]
        total_sum += sum_line_multiplied
    return total_sum

# programa:
print("Cria uma matriz quadrada... \n")
n = int(input("Insere a sua dimensão N -> "))

# ler matriz NxN
matriz_NxN = []
for i in range(n):
    matriz_NxN.append([])
    for j in range(n):
        elem = float(input(f"Introduza o elemento ({i+1},{j+1}) da matriz quadrada de dimensão {n} -> "))
        matriz_NxN[i].append(elem)

print("Multiplicando a soma de todos os elementos de cada linha pelo elemento da diagonal principal da própria linha,")
print(f"o resultado final dessas operações é aproximadamente {mult_lineElemsByDiagonalElems(matriz_NxN, n):.2f}.")
