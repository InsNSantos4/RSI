def encontrar_minas(campo):
    minas = []
    for i, linha in enumerate(campo):
        for j, celula in enumerate(linha):
            if celula == "X":
                minas.append(f"C{i+1},{j+1}")
    return minas

# Matriz de exemplo
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

print(f"As bombas encontram-se nas células: {', '.join(encontrar_minas(campo_minas))}")
