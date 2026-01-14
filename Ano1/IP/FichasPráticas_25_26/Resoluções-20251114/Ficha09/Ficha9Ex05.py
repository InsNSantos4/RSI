# Ficha9 Ex05
'''Faça um programa que efetue as seguintes operações:
a) Crie o seguinte dicionário: dias semana={1:'Domingo', 2:'Segunda-Feira', 3:'Terça-feira', 4:'Quarta-feira', 5:'Quinta-feira', 6:'Sexta-feira', 7:'Sábado'}
b) Crie um dicionário semelhante para os meses do ano: meses ano
c) Peça ao utilizador uma data no formato DS/DM/M/A, em que DS corresponde ao valor inteiro do dia da semana (0 a 7), DM corresponde valor inteiro do mês e A corresponde ao ano. De seguida, apresenta a data por extenso.
Exemplo:
Introduza a data: 4/5/6/2006
Quarta-feira, 5 de Junho de 2006'''

# a)
semana={1:'Domingo', 2:'Segunda-Feira', 3:'Terça-feira', 4:'Quarta-feira', 5:'Quinta-feira', 6:'Sexta-feira', 7:'Sábado'}

# b)
mes={1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}

# c)
d= input('Digite uma data (ex: 7/14/11/2023): ')
data=d.split('/') # obter lista data com base a string de input
# no exemplo: data = ['7','14','11','2023']
# data[0] -> nº do dia semana: '7'
# data[1] dia do mês: '14'
# data[2] -> nº do mês:  '11'
# data[3] -> ano: '2023'
# dia da semana obtem-se no dicionario semana, key= 7 -> semana[7]
#print(data)

# dia da semana obtem-se no dicionario semana, key= 7 -> semana[7]
dsemana = semana[int(data[0])]

# o nome do mês, obtem-se no dicionario mes, key= 11 -> mes[11]
mmes = mes[int(data[2])]

print(f'{dsemana}, {data[1]} de {mmes} de {data[3]} ')