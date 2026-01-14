# Desenvolva uma aplicação que leia um ficheiro de texto contendo uma lista de
# endereços IP e gere um outro ficheiro, contendo um relatório dos endereços IP válidos e
# inválidos.

def validar_ips(ip):
    ip = ip.strip()
    bytes = ip.split('.')
    if len(bytes) != 4:
        return False
    for num in bytes:
        num = int(num)
        if num < 0 or num > 255:
            return False
    return True

#fich_entrada = "lista_IPs_entrada.txt"
#fich_saida = "relatorio_addresses.txt"

validos = []
invalidos = []

# ler ficheiro de entrada
fich_entrada = open("lista_IPs_entrada.txt", 'r')

for address in fich_entrada:
    address = address.strip()   # remove \n
    if validar_ips(address):
        validos.append(address)
    else:
        invalidos.append(address)

fich_entrada.close()

# print(validos)
# print(invalidos)

# gerar ficheiro de saida
fich_saida = open("relatorio_addresses.txt", 'w')
fich_saida.write("[Endereços válidos:]\n")
for address in validos:
    fich_saida.write(address + "\n")

fich_saida.write("\n")

fich_saida.write("[Endereços inválidos:]\n")
for invalid in invalidos:
    fich_saida.write(invalid + "\n")

fich_saida.close()