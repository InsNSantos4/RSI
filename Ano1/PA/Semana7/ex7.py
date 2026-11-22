class LineNotValid(Exception):
    #print(0)
    pass

def print_numbers_InFiles(file):
    
    try:
        with open(file, "r") as f:
        
            for i in f:
                linha= i.strip()
                if linha.isnumeric():
                    print(int(linha)*2)
                else:
                    raise LineNotValid(f"Linha do ficheiro está em branco OU não é um número. Conteúdo da linha --> '{linha}' ")
    except FileNotFoundError:
        print("Ficheiro não existe, não pode ser lido.")
    except LineNotValid as error:
        raise error
    except Exception:
        print("Erro ao tentar abrir o ficheiro em modo leitura.")


try:
    print_numbers_InFiles("./ficheiro.txt")
except LineNotValid as err:
    print("Foi detetado um erro: " + str(err))