def anagramas(palavra, palavra2):
    return sorted(palavra.lower()) == sorted(palavra2.lower())

palavra = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if anagramas(palavra,palavra2):
    print("sao anagramas")
else:
    print("nao sao anagramas")