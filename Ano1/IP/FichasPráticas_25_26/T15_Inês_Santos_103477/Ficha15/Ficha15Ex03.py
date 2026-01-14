# Ficha15 Ex03

fich = open('exercicio3.txt') # não falta ,'r'?

M = H = False
dados = []
c=0
for l in fich:
    l = l.strip()
    c= c +1
    if l == '[Mulheres]':
        M = True
        H = False
        c=0
    elif l == '[Homens]':
        M = False
        H = True
        c=0

    if c >0 and len(l)>0:
        nome,n = l.split('=')
        i,p = n.split(',')
        i = int(i)
        p = int(p)

        aux = ['M'*M+'H'*H,nome,i,p]
        dados.append(aux)

fich.close()
print(dados)

id = [x[2] for x in dados ]
med_id = round(sum(id)/len(id),1)
#print(med_id)

pe = [x[3] for x in dados ]
med_pe = round(sum(pe)/len(pe),1)
#print(med_pe)


id_H = [x[2] for x in dados if x[0] == 'H']
med_id_H = round(sum(id_H)/len(id_H),1)
#print(med_id_H)

id_M = [x[2] for x in dados if x[0] == 'M']
med_id_M = round(sum(id_M)/len(id_M),1)
#print(med_id_M)

pe_H = [x[3] for x in dados if x[0] == 'H']
med_pe_H = round(sum(pe_H)/len(pe_H),1)
#print(med_pe_H)

pe_M = [x[3] for x in dados if x[0] == 'M']
med_pe_M = round(sum(pe_M)/len(pe_M),1)
#print(med_pe_M)

fo =open('medias.txt','w')
fo.write('-- Media de idades –-\n')
fo.write('Global: '+str(med_id)+'\n')
fo.write('Mulheres: '+str(med_id_M)+'\n')
fo.write('Homens: '+str(med_id_H)+'\n')
fo.write('\n-- Media de pesos –-\n')
fo.write('Global: '+str(med_pe)+'\n')
fo.write('Mulheres: '+str(med_pe_M)+'\n')
fo.write('Homens: '+str(med_pe_H))
fo.close()