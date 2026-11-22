def print_to_file(file):
    # path relativo ao base directory
    # absolute path (caminho completo)

    f = open(file, "w")
    for i in range(1,7):
        f.write(str(i) + "\n")
    f.write("\n")
    lista = ["66", "77", "88", "99", "#100", "cem"]
    for l in lista:
        f.write(l + "\n")
    
    f.close()


print_to_file("ficheiro.txt")