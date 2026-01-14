#Ficha9 Ex01

# Lista para armazenar os valores
valores = []

# Leitura de valores
while True:
    valor = input("Digite um valor (ou 'x' para sair): ")
    if valor.lower() == 'x':
        break
    valor = float(valor)
    valores.append(valor)

# Exibição da quantidade de valores lidos
print(f"\nQuantidade de valores lidos: {len(valores)}")

# Exibição dos valores na ordem de introdução
print("Valores na ordem de introdução:", valores)

# Exibição dos valores na ordem inversa
print("Valores na ordem inversa:", valores[::-1])
print("Valores na ordem inversa: ",end = '')
for i in range(len(valores)):
    print(valores[-i-1], end= ' ' )
print()

# Cálculo e exibição da soma dos valores
soma = sum(valores)
print(f"Soma dos valores: {soma}")

# Cálculo e exibição da média dos valores
media = soma / len(valores)
print(f"Média dos valores: {media:.2f}")

# Contagem e exibição dos valores acima da média
#acima_da_media = sum(1 for valor in valores if valor > media_valores)
acima_media = 0
print("\nValores acima da média: ",end='')
for valor in valores:
    if valor > media:
        acima_media += 1
        print(valor, end=' ')
print(f"\nValores acima da média: {acima_media}")

# Valor de referência para calcular a quantidade de valores abaixo
valor_referencia = float(input("Digite um valor de referência: "))

# Contagem e exibição dos valores abaixo do valor de referência
#    abaixo_referencia = sum(1 for valor in valores if valor < valor_referencia)
print(f"Valores abaixo de {valor_referencia}: ",end = ' ')
abaixo_referencia = 0
for valor in valores:
    if valor < valor_referencia:
        abaixo_referencia += 1
        print(valor, end=' ')

print(f"\nValores abaixo da referência: {abaixo_referencia}")
