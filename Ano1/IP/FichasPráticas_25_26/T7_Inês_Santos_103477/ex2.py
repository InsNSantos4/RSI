# Escreva um programa que dada uma cadeia de caracteres mostre no écran todos os seus
# prefixos. Por exemplo, dada a cadeia de caracteres 'UJI', no écran deve aparecer:
# U
# UJ
# UJI

string = str(input("Introduza uma cadeia de caracteres: "))
print("\n")

i = 0

while i < len(string):
    print(string[0:i])
    i = i+1