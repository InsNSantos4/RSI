# A partir de um dicionário crie um novo em que o papel das chaves e dos valores é invertido.
# Exemplo.
# dic entrada={'porto':'azul','sporting':'verde','benfica':'vermelho'}
# dic saida={'azul':'porto','verde':'sporting','vermelho':'benfica'}

entrada={'porto':'azul','sporting':'verde','benfica':'vermelho'}
print("Dicionário de entrada:", entrada)

saida = dict()
for key in entrada: # iterar o dicionario e imprimir   key e value
    print(key,entrada[key])

for key in entrada: # iterar e ir populando o dicionario de saida
    novo_key = entrada[key]
    novo_value = key
    saida[novo_key]= novo_value

print("Dicionário de saída:",saida)