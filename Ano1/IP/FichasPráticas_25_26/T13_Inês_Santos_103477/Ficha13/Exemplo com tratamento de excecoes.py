

##
##    Se no input inserirmos letras ou floats, o programa tratar esses casos de erro
##    Não termina com erro
##    No ficheiro "Exemplo"está o codigo sem tratamento de excepções
##

notas=[]
i = 0
while i < 5:
    try:
      aux = int(input(f'Introduza a nota do aluno {i}: '))
      notas.append(aux)
      i = i + 1
    except:
        print('Ocorreu um erro. Insira um valor valido')



print('Notas:',notas)
print('Media: ',sum(notas)/len(notas))
