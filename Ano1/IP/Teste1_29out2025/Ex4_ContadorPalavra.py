# 103477 Inês Nunes Santos

phrase = input("frase: ")
word = input("palavra: ")

phrase = phrase.split()
counter_word = 0

for i in phrase:
    if i.lower() == word.lower():
        counter_word += 1

print("Nº de ocorrências: "+ str(counter_word))
