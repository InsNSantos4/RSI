# Ficha 7 Ex01
# IP Ficha 07  Exercicio 01
# pedrotomesa@ua.pt - RSI
# pop@ua.pt - Cs
#
# 1. Calcule o valor das seguintes expressões na ordem indicada:
# a) nome = "Introdução à programação e resolução de problemas"
# b) b = nome[0:10]
# c) c = nome[13:24]
# d) d = nome[-9:]
# e) e = nome[-9:-5]
# f) f = nome[-5:-9]
# g) g = nome[:]

print("\n»»»»»»          Ficha 07  Exercicio 01    STRINGS")
print("\n»»»»»» ")
print("»»»»»»  Este programa calcula o valor das seguintes expressões")
print("»»»»»»\n ")
print("\n")

print('nome = "Introdução à programação e resolução de problemas"')
nome = "Introdução à programação e resolução de problemas"

b = nome[0:10]
c = nome[13:24]
d = nome[-9:]
e = nome[-9:-5]
f = nome[-5:-9]
g = nome[:]
h = nome[24:13]
i = nome[1:1]
j = nome[::-1]
k= nome[49:0:-1]
l= nome[49::-1]
print(f'Tamanho da string: {len(nome)}')
print(" b) b = nome[0:10]",b)
print(" c) c = nome[13:24]",c)
print(" d) d = nome[-9:]",d)
print(" e) e = nome[-9:-5]",e)
print(" f) f = nome[-5:-9]",f)
print(" g) g = nome[:]",g)
print(" h) h = nome[24:13]",h)
print(" i) i= nome[1:1]",i)
print(" j) j= nome[::-1]",j)
print(" k) k= nome[49:0:-1]",k)
print(" l) l= nome[49::-1]",l)
# fim do programa