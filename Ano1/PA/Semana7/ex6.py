
def print_numbers_InFiles(file):
    
    try:
        with open(file, "r") as f:
        
            for i in f:
                linha= i.strip()
                if linha.isnumeric():
                    print(int(linha)*2)
                else:
                    print(0)
    except FileNotFoundError:
        print("Ficheiro não existe, não pode ser lido.")
    except Exception:
        print("Erro ao tentar abrir o ficheiro em modo leitura.")

print_numbers_InFiles("./ficheiro.txt")
