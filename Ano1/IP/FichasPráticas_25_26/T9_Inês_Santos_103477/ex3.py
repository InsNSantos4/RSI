# Crie o seguinte dicionário de linguagens de programação e respetivos autores:
# autor = {"php":"Rasmus Lerdorf","perl":"LarryWall","tcl":"John Ousterhout","awk":"Brian
# Kernighan","java":"James Gosling","parrot":"Simon Cozens","python":"Guido van
# Rossum"}.
# Peça nomes de linguagens de programação ao utilizador e apresente o nome do
# respetivo autor no ecrã.

language_authors = {
    "php":"Rasmus Lerdorf",
    "perl":"LarryWall",
    "tcl":"John Ousterhout"
    ,"awk":"Brian Kernighan"
    ,"java":"James Gosling",
    "parrot":"Simon Cozens"
    ,"python":"Guido van Rossum"
}

lang_prog = input("Introduza o nome de uma linguagem de programação: ")

author_found = False

for language, author in language_authors.items():
    if lang_prog != language or lang_prog.lower() != language:
        continue
    else:
        author_found = True
        print(f"O autor da linguagem de programação {lang_prog} é {author}.")

if not author_found:
    print("Não existe no dicionário nenhum autor da linguagem de programação inserida.")