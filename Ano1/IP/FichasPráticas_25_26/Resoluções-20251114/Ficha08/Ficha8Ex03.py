#Ficha 8 Ex 3

# Escreva um programa que leia as notas de um conjunto de 20 alunos e as guarde numa lista.
# Calcular a média das notas e o número de notas acima da média.

print("Este programa lê as notas de X alunos e calcula a sua média.")
n_alunos=int(input('Quantos alunos? :'))
notas=[]
soma = 0
for a in range(n_alunos):
    n = int(input(f'Nota do aluno {a+1:2}: ' ))
    soma += n
    notas.append(n)

media = round(soma / n_alunos)
print(f'Média das notas: {media}')
print('Notas acima da média: ')

notas_acima= 0
for a in range(len(notas)):
    if notas[a] > media:
        print(f' Aluno {a +1}: {notas[a]} ')
        notas_acima += 1
print('Nº de Notas acima da média', notas_acima)

#Outra forma
notas_acima= 0
for znota in notas:
    #print(znotz)
    if znota > media:
        notas_acima += 1
print('Nº de Notas acima da média', notas_acima)