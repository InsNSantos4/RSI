
##
##    Se no input inserirmos letras ou floats, o programa termina com eero
##    Ver em ficheiro "Exemplo com tratamento de excecoes" solução para tratar esses casos de erro
##
##

notas=[]
i = 0
while i < 5:
    try:
        aux = int(input(f'Introduza a nota do aluno {i}: '))
    except ValueError:
        print('Numero Inválido. Repita a entrada.')
        continue
    notas.append(aux)
    i = i + 1

print('Notas:',notas)
print('Media: ',sum(notas)/len(notas))
