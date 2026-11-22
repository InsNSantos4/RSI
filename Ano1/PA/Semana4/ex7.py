import sys

class Pessoa():
    pass

pessoa_1 = Pessoa()
pessoa_2 = Pessoa()
a = pessoa_1
lista = []

lista.append(a)

print(sys.getrefcount(pessoa_1))

# se o is é verdade, o == tmb tem que ser verdade.