#Matriz 4x3

print("\nMatriz de 4x3")
print()
mat = [
        ["C1,1", "C1,2", "C1,3"],
        ["C2,1", "C2,2", "C2,3"],
        ["C3,1", "C3,2", "C3,3"],
        ["C4,1", "C4,2", "C4,3"],
      ]
print()
print("mat:      ",mat)
print()
linha1 = mat[0]
linha2 = mat[1]
linha3 = mat[2]
linha4 = mat[3]
print("Linha 1 - mat[0]   :",mat[0])
print("Linha 2 - mat[1]   :",mat[1])
print("Linha 3 - mat[2]   :",mat[2])
print("Linha 4 - mat[3]   :",mat[3])
print()

print("mat(2,1) : linha2[0] ",linha2[0])
print("mat(2,1) : mat[1][0] ",mat[1][0])
print()
L2C3 = mat[1][2]
print(": Linha4 - Col3 mat[3][[2]   :",mat[3][2])
print()
Col1=[mat[0][0], mat[1][0], mat[2][0],mat[3][0]]
print('Col1=[mat[0][0], mat[1][0], mat[2][0],mat[3][0]] :' ,Col1)
print()
Col3=[mat[0][2], mat[1][2], mat[2][2],mat[3][2]]
print('Col3=[mat[0][2], mat[1][2], mat[2][2],mat[3][2]] :' ,Col1)

print()
for l in range(4): # linhas 1-2-3-4
    for col in range(3): # colunas 1-2-3
        print(mat[l][col],' ',end='')
    print()

print()
for l in range(4): # linhas 1-2-3-4
    for col in range(3): # colunas 1-2-3
        print(mat[l][col],end=' ')
    print()