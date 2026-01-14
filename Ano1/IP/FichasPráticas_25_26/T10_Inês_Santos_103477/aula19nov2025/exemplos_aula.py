# Exemplo do 1º exercício de Listas, do Ricardo: 

for pair in zip(*matriz): # o asterisco "desencapsula"/desempacota uma lista/a variável que aparece à frente
    print(pair)


import math

type(42)

# Evitar repetir código
#Organizar o código/programa em blocos lógicos
# Mais fácil de manter
# Dividir programas maiores em partes mais pequenas
# Exemplos de funções: list(), len(), print(), etc

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I'll sleep all night and work all day.")
    
print_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)

"spam" * 4
print("spam" * 4)

print_twice("spam" * 4)
print_twice(math.cos(math.pi)) # cos(pi) = -1



def main():
    print("Olá, este é o programa principal")
    
if __name__ == "__main__":
    main()
    
# A variável especial __name__ é criada automaticamente pelo Python em 
# todos os ficheiros (.py) quando são executados ou importtados.
# Serve para o Python saber como o ficheiro está a ser utilizado.

# Quando o programa é executado diretamente:
# __name__ fica com o valor"__main__" -> então, a função main() é chamada

# Quando é importado de outro ficheiro:
# __name__ fica com o nome do módulo -> a função main() não é chamada



# A diretiva import programa, sem a "estrutura main" executa o código 
# que está no módulo programa.