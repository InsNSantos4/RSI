# Ficha9 Ex03

"""Crie o seguinte dicionário de linguagens de programação e respetivos autores:
autor = {"php":"Rasmus Lerdorf","perl":"LarryWall","tcl":"John Ousterhout","awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens","python":"Guido van Rossum"}.
Peça nomes de linguagens de programação ao utilizador e apresente o nome do respetivo autor no ecrã."""

# Criar e carregar dicionario
autor = {"php":"Rasmus Lerdorf","perl":"LarryWall","tcl":"John Ousterhout","awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens","python":"Guido van Rossum"}

while True:
    lang = input('Digite a linguagem (x para sair): ')
    lang = lang.lower()
    if lang =='x':
        break
    elif lang in autor:
        print(f' Linguagem "{lang.capitalize()}": Autor: {autor[lang]} ')
    else:
        print(f' Linguagem "{lang.capitalize()}" não encontrada')
    print()
