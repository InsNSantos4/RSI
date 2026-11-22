def write_file_with(file):

    with open(file, "w") as f:
        for i in range(1,7):
            f.write(str(i) + "\n")
        f.write("\n")
        lista = ["66", "77", "88", "99", "#100", "cem"]
        for l in lista:
            f.write(l + "\n")

write_file_with("ficheiro.txt")

def print_file_with(file):
    
    with open(file, "r") as f:
    
        for i in f:
            print(i.strip())

print_file_with("ficheiro.txt")