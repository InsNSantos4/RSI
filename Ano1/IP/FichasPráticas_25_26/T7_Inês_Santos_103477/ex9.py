# Escreva um programa que dada uma cadeia de caracteres e um número k determine
# quantas palavras de dimensão k se encontram na cadeia de caracteres.

string = input("Introduza uma string: ")
k = int(input("Introduza um número k: "))

k_number_words = 0
i = 0

# if k <= len(string):
#     while i < len(string):
#         for slice in range(i, len(string), k):
#             if slice == k:
#                 k_number_words +=1
#         i += 1
#     print("Número de palavras de dimensão "+ str(k)+ " na palavra "+ string+": "+ str(k_number_words))
# else:
#     print("Erro: número k introduzido é maior do que o número de caracteres da string introduzida.")

if k <= len(string):
    while i < len(string):
        if(len(string[i:i+k]) == k):
            k_number_words += 1
        i = i + 1
    print("Número de palavras de dimensão "+ str(k)+ " na palavra "+ string+": "+ str(k_number_words))
else:
    print("Erro: número k introduzido é maior do que o número de caracteres da string introduzida.")