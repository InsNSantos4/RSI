# Ficha 15 Ex01   ---->    ciclo for, percorre o ficheiro aberto
#

def ver_ip(ip): #recebe string  "234.23.0.12"
    l_end = ip.split('.')
    if len(l_end) != 4:
        return False
    for i in l_end:
        y = int(i)
        if y < 0 or y> 255:
            return False
    return True

ficheiro =  'IP_in1.txt'
fi = open(ficheiro,'r')

ip_ok =[]
ip_not_ok =[]

for linha in fi: #  <--- Percorre o ficheiro linha a linha (uma linha por ciclo)
                        #  e guarda (como string na variavel linha - iterador)
    linha=linha.strip()  # <--- eliminar o caracter de mudança de linha, indicador do final de linha
    if ver_ip(linha):  # ip válido - a função ver_ip() retorna True
        ip_ok.append(linha)
    else:   # ip inválido - a função ver_ip() retorna False
        ip_not_ok.append(linha)

fi.close() # fecho do ficheiro
print('ok    :', ip_ok )
print('not ok:', ip_not_ok)

#criação do ficheiro de output:
fich_out = 'IP_out.txt'
fo=open(fich_out,'w')

cab = '[Endereços válidos:]\n'
fo.write(cab)
for lo in ip_ok:
    line = str(lo)+str('\n')   # adicionar o final de linha
    fo.write(line)

cab = '\n[Endereços inválidos:]\n'
fo.write(cab)
for lo in ip_not_ok:
    line = str(lo)+str('\n')
    fo.write(line)