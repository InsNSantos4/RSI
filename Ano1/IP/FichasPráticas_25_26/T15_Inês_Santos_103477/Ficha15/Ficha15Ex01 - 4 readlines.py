# Ficha 15 Ex01   ---->    readlines -> cria lista de uma só vez
#                Cada linha do ficheiro  cria  um elemento na lista

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
linhas = fi.readlines()  #  <----------  readlines -> cria lista (linhas). Cada linha é um elemento
fi.close()
ip_ok =[]
ip_not_ok =[]
for l in linhas:
    l=l.strip()
    if ver_ip(l): # ip válido - a função ver_ip() retorna True
        ip_ok.append(l)
    else:  # ip inválido - a função ver_ip() retorna False
        ip_not_ok.append(l)

print('ok    :', ip_ok )
print('not ok:', ip_not_ok)

fich_out = 'IP_out.txt'
fo=open(fich_out,'w')

cab = '[Endereços válidos:]\n'
fo.write(cab)
for lo in ip_ok:
    linha = str(lo)+str('\n')
    fo.write(linha)

cab = '\n[Endereços inválidos:]\n'
fo.write(cab)
for lo in ip_not_ok:
    linha = str(lo)+str('\n')
    fo.write(linha)