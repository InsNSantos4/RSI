def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

# Exemplo de teste
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sao_anagramas(palavra1, palavra2):
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")
