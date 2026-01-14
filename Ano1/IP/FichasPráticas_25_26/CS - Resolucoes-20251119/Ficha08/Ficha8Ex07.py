# Ficha 8 Ex 07

# Escreva um programa que para um conjunto de registos de consumo de combustível de
# uma dada viatura, apresente a média aos 100 km. Os registos serão introduzidos pelo
# utilizador até um máximo de 10 registos, na seguinte forma:
# nº de km percorridos # nº litros de combustível gastos
# O processo de leitura de registos de consumo termina quando o utilizador introduzir um
# registo com a forma “0 # 0”, ou forem introduzidos 10 registos. Valide os dados de
# entrada.

print('Introduza os Km e litros de consmumo na forma kkk#ll  (0#0 para terminar): ')
i = 0

km = []
litros =[]
while i < 10:
    a = input(f'Registo {i+1:2}: ')
    ra = a.split('#')
    # validação:
    if (len(ra) != 2) or (not ra[0].isdigit()) or (not ra[1].isdigit()):
        print(' Dados inválidos, introduza dados corretos!')
        continue
    #saida :
    if a == '0#0':
        break
    #dados ok
     #converter para inteiro e adicionar às listas:
    km.append(int(ra[0]))
    litros.append(int(ra[1]))
    i += 1

#print(km)
#print(litros)

#cáculo:
total_km = sum(km)
total_litros=sum(litros)
media= (total_litros / total_km) *100

#saída de dados:
print(f' Consumo aos 100km: {media:.2f}  - ({total_km}km {total_litros}l )')

