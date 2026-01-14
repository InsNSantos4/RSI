# Programa que armazene dois números em variáveis e troque os valores das variáveis

print("Introduza um numero:")
a = float(input())
print("O primeiro numero que introduziu foi " + str(a))
print('\n')

print('Introduza um novo numero:')
b = float(input())
print("O segundo numero que introduziu foi " + str(b))
print('\n')

c = a
a = b
b = c

print("O primeiro numero passou a " + str(a) + " e o segundo numero passou a " + str(b))