# Escreva um programa que peça duas cadeias de caracteres e determine se a
# segunda é um prefixo da primeira. Exemplo: 'hidro' é um prefixo de 'hidro-planador'.

string_1 = str(input("Introduza uma cadeia de caracteres: "))
string_2 = str(input("Introduza uma cadeia de caracteres: "))
print("\n")

string_1.lower
string_2.lower

if(string_1.startswith(string_2)):
    print("'"+string_2 + "' é prefixo de '" + string_1+"'.")
else:
    print("'"+string_2 + "' não é prefixo de '" + string_1+"'.")

# for letter in string_1:
#     for letters in string_2:
#         if string_2[:string_2.find(letter)] in string_1[:len(string_1)-1]:
#             #print(string_2[:string_2.find(letter)] +" é um prefixo de " + string_1)
#             pass
#         #print(string_2[:string_2.find(letter)] +" é um prefixo de " + string_1)
#     print(string_2[:string_2.find(letter)] +" é um prefixo de " + string_1)