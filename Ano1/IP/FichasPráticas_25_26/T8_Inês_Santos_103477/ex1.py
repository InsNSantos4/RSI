# Faça um programa que peça valores ao utilizador e construa uma
# matriz de N x N inteiros. 
# O valor de N também deve ser pedido ao utilizador. 
# Uma vez construída a matriz, o seu programa deverá imprimir a 
# respetiva matriz transposta.

print("Construção de uma matriz de tamanho NxN : \n")

size = int(input("Introduza o valor de N: "))

matriz = []

# construção da matriz n x n
for i in range(0,size):
    matriz.append([])
    for j in range(0,size):
        element = input(f"Introduza o elemento [{i+1},{j+1}]: ")
        matriz[i].append(element)

print(matriz)
print()

# Exemplo do 1º exercício de Listas, do Ricardo (aula 19 nov 2025): 
# for pair in zip(*matriz): # o asterisco "desencapsula"/desempacota
#                           # uma lista/a variável que aparece à frente
#    print(pair)

print("Matriz Transposta: ")

# imprimir matriz transposta
for i in range(size):
    for j in range(size):
        print(f" {matriz[j][i]} ", end = ' ')
    print()