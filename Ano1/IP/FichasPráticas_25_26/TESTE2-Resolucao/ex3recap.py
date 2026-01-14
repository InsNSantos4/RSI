# def encontrar_minas(campo):
#     minas = []
#     #print(len(campo))
#     for i, linha in enumerate(campo):
#         #print(len(campo[☻i9])) vou guardar isto pq não sei em que é que cliquei para fazer o emoji
#         #print(len(campo[i]))
#         for j, celula in enumerate(linha):
#             if celula == "X":
#                 minas.append(f"Linha {i+1}, Digito {j+1}")
#     return minas

def encontrar_minas(campo):
    minas = []
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            if campo[i][j] == "X":
                minas.append(f"Linha {i+1}, Digito {j+1}")
    return minas

campo_minas = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 1, 0, 0, 0, 0],
    [2, "X", "X", 2, 2, 1, 1, 0],
    ["X", 3, 3, "X", 2, "X", 2, 1],
    [2, 2, 3, 3, 4, 3, "X", 1],
    [1, "X", 2, "X", "X", 2, 1, 1],
    [1, 1, 3, 3, 3, 1, 0, 0],
    [0, 0, 1, "X", 1, 0, 0, 0],
]

print(f"As bombas encontram-se nas células: {' | '.join(encontrar_minas(campo_minas))}")