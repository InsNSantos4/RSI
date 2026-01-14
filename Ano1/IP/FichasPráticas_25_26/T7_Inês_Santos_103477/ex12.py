# Um texto tem os parêntesis bem estruturados se por cada parêntesis aberto existe outro
# que o encerra. Por exemplo, a frase 'Este (é (um) (exemplo (de) ((cadeia de caracteres)
# bem )) estruturada)' está bem estruturada, enquanto as seguintes cadeias de caracteres
# não estão: 'uma cadeia de caracteres)', '(outra cadeia de caracteres',') ainda outra (
# cadeia de caracteres'. 
# Escreva um programa que determine se os parêntesis estão bem
# estruturados numa cadeia de caracteres.

string = str(input("Introduza uma cadeia de caracteres: "))
i = 0
count_parentesis = 0
bem_estruturado = True

while i < len(string):
    if string[i] == "(":
        count_parentesis += 1
        bem_estruturado = False
    elif string[i] == ')':
        count_parentesis -= 1
        bem_estruturado = False
        
    if count_parentesis != 0:
        bem_estruturado = False
    else:
        bem_estruturado = True
        
    i = i + 1
    
if bem_estruturado:
    print("Os parêntesis na cadeia \""+ string+"\" estão bem estruturados.")
else:
    print("Os parêntesis não estão bem estruturados.")