# Ficha9 Ex08
'''A partir de um dicionário crie um novo em que o papel das chaves e dos valores é invertido.
Exemplo.
dic entrada={'porto':'azul','sporting':'verde','benfica':'vermelho'}
dic saida={'azul':'porto','verde':'sporting','vermelho':'benfica'}'''

dic= {'porto':'azul','sporting':'verde','benfica':'vermelho'}
print(f'Dicionario de entrada: {dic}')

dic_out={}

for key in dic:
    print(key,dic[key])
for key in dic:
    value = dic[key]
    dic_out[value]=key

print(f'Dicionario de saida: {dic_out}')

#
# b=dic.items()
# c=list(dic.items())
# e=tuple(dic.items())
# f=dic.keys()
# g=list(dic.keys())
# h=tuple(dic.keys())
# i=dic.values()
# j=list(dic.values())
# k=tuple(dic.values())
