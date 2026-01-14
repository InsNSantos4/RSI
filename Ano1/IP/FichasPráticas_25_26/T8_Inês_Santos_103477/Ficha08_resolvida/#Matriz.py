#Matriz 4x3

mat = [
        ['A', 'B', "C"],
        ['1', '2', '3'],
        ['D', 'E', "F"],
        ['4', '5', '6'] ]

# imprime cada elemento da matriz M (que é a lista correspondente à linha)
print('imprime cada elemento da lista M (cada elemento é a lista correspondente à linha)')
for linha in range(4):
    # aux = mat[linha]
    print(mat[linha])


print('imprime cada elemento de cada linha da matriz M' )
for linha in range(4):
    for coluna in range(3):
        print(mat[linha][coluna],end= ' ')
    print()
## Criar Matriz   mat1
mat1=[]
for linha in range(4):
    mat1.append( [])
    for coluna in range(3):
        mat1[linha].append('')

print('\nprint da matriz M')
print(mat)
print('\nprint da matriz M1')
print(mat1)

## Criar Matriz   mat2
# copia mat1 e transforma em minusculas ao acrescentar cada elemento na M2
mat2=[]
for linha in range(4):
    mat2.append( [])
    for coluna in range(3):
        mat2[linha].append(mat[linha][coluna].lower()) # transforma em minusculas ao acrescentar cada elemento na M2

print('\nprint da matriz M2   passou a minusculas a matriz M')
print(mat2)
