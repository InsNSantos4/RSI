# Programa que calcule a idade de uma pessoa com base na sua data de 
# #nascimento e o ano atual. A resposta do programa deverá ser 
# # “ A Ana tem 25 anos”

import datetime
# import os

print("Em que ano nasceu?")
birth_year = int(input())
print('\n')

x = datetime.datetime(2000, 6, 1)

current_year = datetime.datetime.now().year
print("Estamos no ano " + str(current_year))

current_age = current_year - birth_year

#age = datetime.datetime.now() - x

print("A Ana tem " + str(current_age) + " anos.")