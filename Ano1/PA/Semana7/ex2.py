def print_file_onScreen(file):
    
    f = open(file, "r")
    
    
    for i in f:
        # A função strip vai eliminar a linha "\n" que o print 
        #   introduz automaticamente no final, ao imprimir cada linha
        # se quiseres apenas remover o \n final
        print(i.rstrip())

    f.close()

print_file_onScreen("ficheiro.txt")