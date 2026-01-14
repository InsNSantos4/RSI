#
# POP outubro 2022
#
# IP Ficha 04  Exercicio 03
#
# Multas por Excesso de Velocidade
# 3.	Muitas comunidades têm agora sinais "radar" que informam os condutores qual a sua velocidade,
#  na esperança de que eles possam abrandar.
# Pretende-se assim imprimir uma mensagem para um sinal de "radar".
# A mensagem exibirá informações para o condutor tendo por base a sua velocidade e de acordo com a seguinte tabela:
#   Km/h acima do limite	Multa (€)
#    1 – 20	                120
#   21 – 30	                250
#   Superior a 30	        500
#
# Escreva um programa que receba como entrada dois inteiros, o primeiro relativo ao limite
# de velocidade na estrada e o segundo relativo à velocidade do veículo, e retorne se o
# condutor está a infringir o código da estrada (“Infrator”) ou não (“Cumpridor”). E em
# caso de estar a infringir o código deverá indicar também o valor da multa.


print("\n»»»»»» ")
print("»»»»»»  Este programa lê o limite de velocidade e a velocidade do veículo")
print("»»»»»»   retorna se o codigo da estrada é cumprido ")
print("»»»»»»   e qual o valor da multa em caso de infração.")
print("»»»»»»\n ")
print("\n")

# Entrada de dados
limite_vel = int(input("Entre o limite de velocidade  (Km/h): "))
vel_veiculo = int(input("Entre a velocidade do veículo (Km/h): "))

# Verificação se há infração / multa
if vel_veiculo <= limite_vel:
    print(' Cumpridor ')
elif vel_veiculo <= limite_vel + 20:
    print(' Infrator: multa de €120   Excedeu o limite de velocidade em', vel_veiculo - limite_vel,'Km/h')
elif vel_veiculo <= limite_vel + 30:
    print(' Infrator: multa de €250   Excedeu o limite de velocidade em', vel_veiculo - limite_vel,'Km/h')
else:
    print(' Infrator: multa de €500   Excedeu o limite de velocidade em', vel_veiculo - limite_vel,'Km/h')

# fim do programa
