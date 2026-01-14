# Escreva um programa que peça uma cadeia de caracteres e apresente no écran todas as
# suas subcadeias de caracteres de comprimento 3. Por exemplo, dada a cadeia de
# caracteres 'Programação', no écran deve surgir:
# Pro
# rog
# ogr
# gra
# ram
# ama
# maç
# açã
# ção

string = str(input("Introduza uma cadeia de caracteres: "))
print("\n")

i = 2

while i <= len(string):
    print(string[i-3:i])
    i+=1
    
# The `# OU` in the code is a comment that suggests an alternative way to achieve the same result. It
# indicates that the following block of code is an alternative implementation to the previous one
# using a different approach. In this case, it provides a different way to iterate over the string and
# print its substrings of length 3.
# OU
# texto = input("Introduza uma cadeia de caracteres: ")

# i = 0
# while i <= len(texto) - 3:
#     print(texto[i:i+3])
#     i += 1
