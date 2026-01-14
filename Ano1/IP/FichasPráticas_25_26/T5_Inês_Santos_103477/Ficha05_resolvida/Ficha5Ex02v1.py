#
# POP outubro 2023
#
# IP Ficha 05  Exercicio 02
#


print("\n»»»»»»          Ficha 05  Exercicio 02")
print("\n»»»»»» ")
print("»»»»»»  Este programa imprime no ecrã todos os números inteiros de 1 a 100")
print()

x=input('==> Prima "ENTER" para continuar <==')
print()
print("»»»»»»  a) Utilizando o ciclo 'while':")
i = 1
while i <= 100:
    print(i)
    i = i + 1
print("»»»»»»\n ")
print("\n")
print()


input('==> Prima "ENTER" para continuar <==')
print()

print("»»»»»»  b) Utilizando o ciclo 'for':")
for i in range(1, 101):
    print(i)
print("»»»»»»\n ")

input('==> Prima "ENTER" para continuar <==')
print()
print("»»»»»»  c) while em ordem inversa:")
i=100
while i >= 1:
    print(i)
    i = i - 1


input('==> Prima "ENTER" para continuar <==')
print()
print("»»»»»»  c) for em ordem inversa:")
for i in range(100, 0, -1):
    print(i)
print("»»»»»»\n ")


# fim do programa
