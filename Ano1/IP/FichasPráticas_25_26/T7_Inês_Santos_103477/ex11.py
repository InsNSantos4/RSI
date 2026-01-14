# Escreva um programa que apresente os números contidos numa cadeia de caracteres.
# Por exemplo 'um 1 e dois 201 e 33' contém os números 1, 201 e 33.

string = str(input("Introduza uma cadeia de caracteres: "))
i = 0

splitted = string.split()
#print(splitted)

numbers_in_string = []

for str in splitted:
    if str.isnumeric():
        numbers_in_string.append(str)

if len(numbers_in_string) > 0:
    print("A string \""+ string+ "\" contém os números:")
    for s in numbers_in_string:
        print(s)
else:
    print("Esta string não tem números.")