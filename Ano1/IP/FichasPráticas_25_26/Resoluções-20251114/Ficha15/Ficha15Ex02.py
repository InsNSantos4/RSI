# Ficha 15 Ex02

# função que retona MB
def mb(bytes):
    megaBytes = bytes/(1024**2)
    MBytes = str(round(megaBytes,2))+'  MB'
    return MBytes

def percent(i,lista):
    per = round(lista[i]/sum(lista)*100,2)
    percent_value = str(per)+'%'
    return percent_value



#Leitura do ficheiro  e carregamento na lista dados[]
nome_ficheiro_entrada = 'users.txt'
fi = open(nome_ficheiro_entrada,'r')
dados = fi.readlines()
fi.close()

#inicialização das listas para receber os dados tratados
users=[]
espaco = []
megas=[]

# tratamento dos dados user a user
for l in dados:
    l=l.strip()
    a,b = l.split()
    users.append(a)
    aux = int(b)
    espaco.append(aux)
    megas.append(mb(aux))

total = sum(espaco)
percent_espaco=[]
for i in range(len(espaco)):
    per = round(espaco[i]/total*100,2)
    percent_espaco.append(percent(i,espaco))

# print(users)
# print(espaco)
# print(megas)
# print(percent_espaco)

fo = open('relatorio.txt','w')
l0 = 'ACME Inc.Uso do espaço em disco pelos usuários\n' \
     '----------------------------------------------\n'\
     'Nr.\tUtilizador\t Espaço utilizado\t % do uso'
print(l0)
fo.write(l0+'\n')

for i in range(len(users)):
    l = str(i+1)+'\t'+users[i].ljust(17,' ')+ megas[i].rjust(12,' ')+percent_espaco[i].rjust(12,' ')
    print(l)
    fo.write(l+'\n')

fo.write('\n')
l = 'Espaço total ocupado:   '+mb(total).rjust(15)
print('\n'+l)
fo.write(l+'\n')

l = 'Espaço médio ocupado:   '+mb(total/len(users)).rjust(15)
print(l)
fo.write(l+'\n')


