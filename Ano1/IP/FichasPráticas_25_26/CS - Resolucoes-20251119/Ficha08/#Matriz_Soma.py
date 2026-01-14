# Soma de 2 Matrizes

M1 = [ [1,8,4],
       [12,7,9] ]

print()

n_linhas  = 2  # len(M1)
n_colunas = 3  # len(M1[0])

print('Print da Matriz M1: ')
print(M1)
for linha in range(n_linhas):
    for coluna in range(n_colunas):
        print(M1[linha][coluna],end=' ')
    print()



M2 = [ [9,5,-4],
       [6,4,-1] ]

print()
print('Print da Matriz M2: ')
print(M2)
for linha in range(n_linhas):
    for coluna in range(n_colunas):
        print(M2[linha][coluna],end=' ')
    print()


# Soma
print()
print('Print da soma M1+M2: ')
for linha in range(n_linhas):
    for coluna in range(n_colunas):
        soma = (M1[linha][coluna] + M2[linha][coluna])
        print(soma,end=' ')
    print()

# Matriz soma
M_soma=[]
for linha in range(n_linhas):
    M_soma.append([])
    for coluna in range(n_colunas):
        soma = (M1[linha][coluna] + M2[linha][coluna])
        M_soma[linha].append(soma)

print()
print(M_soma)