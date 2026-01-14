# Escreva um programa que leia as notas de um conjunto de 20 alunos e as guarde numa
# lista. Calcular a média das notas e o número de notas acima da média.

student_grades = []
sum = 0
nota_valida = False

for i in range(20):
    nota = float(input(f"Introduza a nota do aluno {i+1} -> "))
    nota_valida = False
    while nota_valida == False:
        if (nota >= 0 and nota <= 20): 
            student_grades.append(nota)
            sum += student_grades[i] # ir somando as notas // ou soma += nota
            nota_valida = True
        else:
            print("Erro: nota do aluno tem que ser um valor entre 0 e 20.")
            nota = float(input(f"Introduza a nota do aluno {i+1} -> "))
            nota_valida = False

average = sum/20    # média das notas
num_grades_above_average = 0

# Cálculo do nº de notas acima da média:
for i in student_grades:
    if i > average:
        num_grades_above_average += 1

print(f"Há {num_grades_above_average} notas acima da média ({average:.2f}) no conjunto de 20 alunos.")