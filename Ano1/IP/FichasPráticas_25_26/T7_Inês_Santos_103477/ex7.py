# Escreva um programa que inverta a ordem dos caracteres numa cadeia de caracteres.
# Por exemplo, a cadeia de caracteres 'Introdução à programação e resolução de
# problemas' deve ser convertida na cadeia de caracteres 'samelborp ed oãçuloser e
# oãçamargorp à oãçudortnI '.

string = input("Introduza uma cadeia de caracteres: ")
print("\n")

string_invertida = string[::-1]

print(string_invertida)