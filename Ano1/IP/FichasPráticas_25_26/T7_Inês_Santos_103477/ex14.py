# Uma palavra diz-se alfabética se todas as letras estão ordenadas alfabeticamente. Por
# exemplo, 'amor' é uma palavra alfabética. Escreva um programa que determine se uma
# palavra é alfabética.

word = input("Introduza uma palavra: ")
i = 0
ordenada = True
word = word.lower()

if len(word) >= 0:
    while i < len(word)-1:
        if word[i] < word[i+1]:
        # if word[i:] < word[i+1:]:   # funciona com qualquer um destes ifs
            ordenada = True
        else:
            ordenada = False
        i = i + 1
        
    if ordenada == True:
        print (word +" é uma palavra alfabética.")
    else:
        print (word +" não é uma palavra alfabética.")
else:
    print("Erro: não é uma palavra.")