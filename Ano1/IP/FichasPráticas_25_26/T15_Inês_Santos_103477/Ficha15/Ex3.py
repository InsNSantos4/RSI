# Ficha15 Ex03

fich = open('exercicio3.txt') # não falta ,'r'?

M = H = False
idade_H = []
idade_M = []
peso_M = []
peso_H = []
for linha in fich:
    l = linha.strip()
    if l == '[Mulheres]':
        M = True
        H = False
        continue
    elif l == '[Homens]':
        M = False
        H = True
        continue

    if len(l)>0:
        nome,n = l.split('=')
        i,p = n.split(',')
        i = int(i)
        p = int(p)

        if M :
            peso_M.append(p)
            idade_M.append(i)

        if H :
            peso_H.append(p)
            idade_H.append(i)

fich.close()


# a)
med_id_M = round(  sum(idade_M)/len(idade_M) )
med_id_H = round(  sum(idade_H)/len(idade_H)  )
med_id_global = round(  (sum(idade_M)+ sum(idade_H) ) / (len(idade_M) +len(idade_H))   )

med_peso_M = round(  sum(peso_M)/len(peso_M)  )
med_peso_H = round(  sum(peso_H)/len(peso_H)  )
med_peso_global = round(  (sum(peso_M)+ sum(peso_H) ) / (len(peso_M) +len(peso_H))  )

# b)
fo =open('exercicio3_medias.txt','w')
fo.write('-- Media de idades –-\n')
fo.write(f'Global: {med_id_global}\n')
fo.write(f'Mulheres: {med_id_M}\n')
fo.write(f'Homens: {med_id_H} \n')
fo.write('\n-- Media de pesos –-\n')
fo.write(f'Global: {med_peso_global}\n')
fo.write(f'Mulheres: {med_peso_M}\n')
fo.write(f'Homens: {med_peso_H}\n')
fo.close()