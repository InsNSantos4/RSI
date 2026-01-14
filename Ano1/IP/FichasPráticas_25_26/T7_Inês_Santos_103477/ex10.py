# Escreva um programa que conte o número de dígitos presentes numa cadeia de
# caracteres. Por exemplo 'um 1 e dois 20 e 3' contém 4 dígitos.

string = str(input("Introduza uma cadeia de caracteres: "))
i = 0
num_digits = 0

while(i < len(string)):
    if(string[i].isdigit()):
        num_digits += 1
    i = i + 1
print("A string "+ str(string)+ " tem "+str(num_digits)+ " dígitos.")