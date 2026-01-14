# Escreva um programa que peça duas cadeias de caracteres e determine se a segunda é
# uma subcadeia de caracteres da primeira. Exemplo: 'drop' é uma subcadeia de
# 'hidroplanador'.

string_1 = str(input("Introduza uma cadeia de caracteres: "))
string_2 = str(input("Introduza uma segunda cadeia de caracteres: "))
print("\n")

if string_2 in string_1:
    print("'"+ string_2+ "' é subcadeia de '"+ string_1+"'.")
else:
    print("'"+ string_2+ "' não é subcadeia de '"+ string_1+"'.")