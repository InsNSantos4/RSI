def bytes_to_megabytes(bytes):
    return bytes / (1024 ** 2)

def space_percentage_byUser(space):
    pass

#Ler users.txt
read_users = open("users.txt", 'r')
dados = read_users.readlines()      # armazenando os dados em memória
read_users.close()

