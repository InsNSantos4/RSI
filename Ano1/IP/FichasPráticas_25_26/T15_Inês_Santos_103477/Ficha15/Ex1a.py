# Validação de IPs

# função para validar IP
def check_ip(ip):
    l_end = ip.split('.') # cria lista, um numero por elemento - split pelo "."
    if len(l_end) != 4:    # se o num de valores for diferente de 4,  --> endereço invalido
        return False
    for num in l_end: # percorre cada nummero
        if  int(num) > 255:  # se num maior que 255 --> endereço inválido
            return False
    return True

fich_in = 'IP_in.txt'      # nome do ficheiro de input
fin = open(fich_in,'r')   # abertura pra leitura

l_ip = fin.readlines()   #leitura -> para lista (readlines), uma linha em cada elemento
fin.close()   # fecho do ficheiro
print(l_ip)

end_ok     =  []    #  inicialiazação de lista para os endereços ok
end_not_ok = []     #   inicialiazação de lista para os endereços not_ok
for endereco in l_ip:  # percorre a lista dos ips para verificar se o IP é válido
    endereco = endereco.strip()  # retira /n se existir
    if check_ip(endereco):
        end_ok.append(endereco)   # se ok, adiciona à lista ok
    else:
        end_not_ok.append(endereco)  # se not ok, adiciona à lista not_ok

print(end_not_ok)
print(end_ok)

fich_out = 'IP_out.txt'  # nome de ficheiro para escrita
fout = open(fich_out,'w')  # abertura de ficheiro para escrita

fout.write('[Endereços válidos:]\n')  # escrita do cabeçalho
for l in end_ok  :
    fout.write(l+'\n')    # escrita linha a linha da lista de endereços ok

fout.write('\n[Endereços inválidos:]\n')   # escrita do cabeçalho
for l in end_not_ok:
    fout.write(l+'\n')    # escrita linha a linha da lista de endereços not ok

fout.close()   # fecho do ficheiro para escrita




