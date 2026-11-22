'''
def write_fileMult3_with(file):

    with open(file, "w") as f:
        for i in range(1,7):
            f.write(str(i) + "\n")
        f.write("\n")
        lista = ["66", "77", "88", "99", "#100", "cem"]
        for l in lista:
            f.write(l + "\n")

write_fileMult3_with("ficheiroMult3.txt")

'''

def print_linesMult3_with(file):

    with open(file, "r") as f:
    
        line_number = 0
        for i in f:
            line_number += 1
            # imprime apenas as linhas múltiplas de 3
            if line_number % 3 == 0:
                # faz apenas o strip do "\n" final
                print(i.rstrip())

print_linesMult3_with("ficheiroMult3.txt")