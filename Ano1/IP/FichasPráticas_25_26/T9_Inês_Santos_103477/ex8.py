# A partir de um dicionário crie um novo em que o papel das chaves e dos valores é
# invertido.
# Exemplo.
# dic entrada={'porto':'azul','sporting':'verde','benfica':'vermelho'}
# dic saida={'azul':'porto','verde':'sporting','vermelho':'benfica'}

dict_entrada = {'porto':'azul','sporting':'verde','benfica':'vermelho'}

print("Dicionário de Entrada: ", dict_entrada)
dict_saida = dict()

# preenchimento do dicionário de saída (dicionário de entrada invertido)
for key, value in dict_entrada.items():
    dict_saida[value] = key

print("Dicionário de Saída: ", dict_saida)