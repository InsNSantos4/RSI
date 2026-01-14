# Escreva um programa que omita as vogais de uma cadeia de caracteres.

string = str(input("Introduza uma cadeia de caracteres: "))

#string.split()
new_string = ""
i = 0

while i < len(string):
    
    lower = string[i].lower()
    if lower not in "aeiouáàéíóúâêôãõ":
        new_string = new_string + string[i]
    i += 1  

print("Cadeia de caracteres sem as vogais: "+ new_string)