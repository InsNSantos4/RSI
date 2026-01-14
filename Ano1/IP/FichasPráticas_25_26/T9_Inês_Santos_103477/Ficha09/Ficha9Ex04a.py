idades = {}

while True:
    nome = input("Digite o nome (ou 'x' para sair): ")

    if nome.lower() == 'x':
        break

    idade = int(input("Digite a idade: "))

    if nome in idades:
        print("Nome já existente. Por favor, insira um nome diferente.")
    else:
        idades[nome] = idade

print("Dicionário completo:")
print(idades)

print("Tamanho do dicionário:", len(idades))

print("Lista de pessoas no dicionário:")
print(list(idades.keys()))

print("Lista de idades no dicionário:")
print(list(idades.values()))

nomes_ordenados = sorted(idades.keys())
print("Nomes ordenados:")
print(nomes_ordenados)

print("Dicionário ordenado por ordem alfabética de nomes:")
for nome in sorted(idades.keys()):
    print(f"{nome}: {idades[nome]}")

nome_remover = input("Digite o nome a ser removido: ")
if nome_remover in idades:
    del idades[nome_remover]
    print("Entrada removida com sucesso.")
else:
    print("Nome não encontrado no dicionário.")

print("Dicionário ordenado após a remoção:")
for nome in sorted(idades.keys()):
    print(f"{nome}: {idades[nome]}")