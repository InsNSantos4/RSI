#
# POP Setembro 2022
#
# IP Ficha 02  Exercicio 06
#
# 		Escreva um programa que calcule a idade de uma pessoa com base na sua data de nascimento e o ano atual.
# 	A resposta do programa deverá ser “Ana tem 25 anos”.

# Ler o ano de nascimento
Ano_nascimento = int(input("Ano de Nascimento?:") )

# Ler o nome
Nome = input("Nome ?:")

# Calculo da idade
Ano_actual = 2023
Idade = Ano_actual - Ano_nascimento

# Print da idade
print("O/a "+Nome+" tem",Idade,"anos de idade.")

