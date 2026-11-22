def print_file_with(file):
    
    try:
        with open(file, "r") as f:
            for i in f:
                print(i.strip())
    except FileNotFoundError:
        print("Ficheiro não existe, não pode ser lido.")
    except Exception:
        print("Erro ao tentar abrir o ficheiro em modo leitura.")

print_file_with("ap.txt")