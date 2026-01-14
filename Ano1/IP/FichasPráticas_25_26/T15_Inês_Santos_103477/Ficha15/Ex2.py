# Ex2

fich_in = 'users.txt'      # nome do ficheiro de input
fin = open(fich_in,'r')   # abertura pra leitura

users = fin.read()   #leitura de todo o ficheiro para a variavel users
fin.close()   # fecho do ficheiro


l_users = users.split('\n')
print(l_users)

# calculo do espaço total
total = 0
for i in l_users:
    nome,espaco = i.split()
    total += int(espaco)

#print (total)

#ficheiro saida:
fich_out = 'users_out.txt'      # nome do ficheiro de saida
fsaida = open(fich_out,'w')   # abertura pra escrita

# cabeçalho:
fsaida.write('ACME Inc.Uso do espaço em disco pelos usuários\n')
fsaida.write('-------------------------------------------------   \n')
fsaida.write('Nº     Utilizador    Espaço Utilizado    % do uso  \n')

# calculo de cada user
numero  = 0
for linha in l_users:
    numero += 1
    nome,espaco = linha.split()
    mb = int(espaco) / (1024**2)
    per = (int(espaco) / total) * 100
    linha = f'{numero:<6} {nome:<15}    {mb:8.2f} MB     {per:6.2f}%'
    #print(linha)
    fsaida.write(linha+'\n')

mb_total = total / (1024**2)
mb_medio = mb_total / numero

fsaida.write(f'\nEspaço total ocupado: {mb_total:8.2f} MB  \n')
fsaida.write(  f'Espaço médio ocupado: {mb_medio:8.2f} MB  \n')
fsaida.close()