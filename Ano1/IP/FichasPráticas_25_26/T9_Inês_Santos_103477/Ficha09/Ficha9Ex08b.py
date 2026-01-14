# A partir de um dicionário crie um novo em que o papel das chaves e dos valores é invertido.
# Exemplo.
# dic entrada={'porto':'azul','sporting':'verde','benfica':'vermelho'}
# dic saida={'azul':'porto','verde':'sporting','vermelho':'benfica'}

entrada={'porto':'azul','sporting':'verde','benfica':'vermelho'}
print("Dicionário de entrada:", entrada)
saida = dict()

# resultado do metodo items() :
print('\n\nentrada.items(): ', entrada.items())

# o metodo items()
for novo_value,nova_key in entrada.items(): # iterar o dicionario e imprimir   key e value
    saida[nova_key] = novo_value

print("Dicionário de saída:",saida)