#Matriz 4x3

mat = [ ]
mat.append(['A', 'b', 'c'])
mat.append(['D', 'A', 'f'])
mat.append(['G', 'h', 'I'])
mat.append(['j', 'K', 'l'])
# matrix = [1,[1,2,3],'sdfsdv',True]


#
# print(mat)
#
#
# for linha in range(4):
#     aux = mat[linha]
#     print(mat[linha])
#     for coluna in range(3):
#         elemento = mat[linha][coluna]
#         print(mat[linha][coluna])
#
# for linha in range(4):
#     for coluna in range(3):
#         print(mat[linha][coluna],end= ' ')
#     print()
## Criar Matriz   mat1
mat1=[]
for linha in range(4):
    mat1.append( []) # [[]]
    for coluna in range(3):
        mat1[linha].append(mat[linha][coluna].lower())

print(mat)
print(mat1)

