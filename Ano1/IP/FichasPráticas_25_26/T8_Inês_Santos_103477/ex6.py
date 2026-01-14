# Escreva um programa que receba uma lista de 10 apostas do euromilhões (ex:
# 1,17,33,44,50,2,6) e a respetiva chave vencedora e indique a lista de prémios a ser
# atribuída.
#
# 1.º Prémio: 5 Números + 2 Estrelas
# 2.º Prémio: 5 Números + 1 Estrela
# 3.º Prémio: 5 Números + 0 Estrelas
# 4.º Prémio: 4 Números + 2 Estrelas
# 5.º Prémio: 4 Números + 1 Estrela
# 6.º Prémio: 3 Números + 2 Estrelas
# 7.º Prémio: 4 Números + 0 Estrelas
# 8.º Prémio: 2 Números + 2 Estrelas
# 9.º Prémio: 3 Números + 1 Estrela
# 10.º Prémio: 3 Números + 0 Estrelas
# 11.º Prémio: 1 Número + 2 Estrelas
# 12.º Prémio: 2 Números + 1 Estrela
# 13.º Prémio: 2 Números + 0 Estrelas
# Sem prémio: Restantes casos

# Cada aposta é um tuplo com 7 valores (porque é imutável)
#               ou uma lista com 7 valores (fazer com listas neste guião)


# Modifique o programa descrito anteriormente de modo a que os números da chave 
# sejam gerados aleatoriamente pelo computador.
# Sugestão: pesquise sobre a geração de números aleatórios em Python.

import random

print("|| EUROMILHÕES ||")

# Chave Vencedora (gerada aleatoriamente pelo computador)
winning_key = []

# Números da Chave
for item_number in range(5):
    key_item_number = random.randint(1, 50)
    winning_key.append(key_item_number)
# Estrelas da Chave
for item_star in range(2):
    key_item_star = random.randint(1, 12)
    winning_key.append(key_item_star)


print("|| EUROMILHÕES ||\nFaça as suas 10 apostas...\n")

bet_list = []
valid_num = False
valid_star = False

for bet in range(10):
    bet_list.append([]) # cada aposta vai ser uma lista com 7 elementos dentro da lista das 10 apostas
    
    # Números
    while valid_num != True:
        for item_number in range(5):
            bet_item_number = int(input(f"Item {item_number+1} da sua aposta (número de 1 a 50) -> "))
            if (1 <= bet_item_number <= 50):
                bet_list[bet].append(bet_item_number)
                valid_num = True
            else:
                print("Erro: Número inválido.")
                bet_item_number = int(input(f"Item {item_number+1} da sua aposta (número de 1 a 50) -> "))
    # Estrelas
    while valid_star == False:
        for item_star in range(2):
            bet_item_star = int(input(f"Estrela {item_star + 1} da sua aposta (número entre 1 e 12) -> "))
            if (1 <= bet_item_star <= 12):
                valid_star = True
                bet_list[bet].append(bet_item_star)
            else:
                print("Erro: Estrela inválida.")
                bet_item_star = int(input(f"Estrela {item_star + 1} da sua aposta (número entre 1 e 12) -> "))

# Descobrir se o utilizador saiu vencedor e qual o prémio:
count_winning_numbers = 0
count_winning_stars = 0

for i in range(10):
    for num in range(5):
        if bet_list[i][num] == winning_key[num]:
            count_winning_numbers += 1
    for star in range(5, 7):
        if bet_list[i][star] == winning_key[star]:
            count_winning_stars += 1

if count_winning_numbers == 5 and count_winning_stars == 2:
    print("Ganhou o 1º Prémio!")
elif count_winning_numbers == 5 and count_winning_stars == 1:
    print("Ganhou o 2º Prémio!")
elif count_winning_numbers == 5 and count_winning_stars == 0:
    print("Ganhou o 3º Prémio!")
elif count_winning_numbers == 4 and count_winning_stars == 2:
    print("Ganhou o 4º Prémio!")
elif count_winning_numbers == 4 and count_winning_stars == 1:
    print("Ganhou o 5º Prémio!")
elif count_winning_numbers == 3 and count_winning_stars == 2:
    print("Ganhou o 6º Prémio!")
elif count_winning_numbers == 4 and count_winning_stars == 0:
    print("Ganhou o 7º Prémio!")
elif count_winning_numbers == 2 and count_winning_stars == 2:
    print("Ganhou o 8º Prémio!")
elif count_winning_numbers == 3 and count_winning_stars == 1:
    print("Ganhou o 9º Prémio!")
elif count_winning_numbers == 3 and count_winning_stars == 0:
    print("Ganhou o 10º Prémio!")
elif count_winning_numbers == 1 and count_winning_stars == 2:
    print("Ganhou o 11º Prémio!")
elif count_winning_numbers == 2 and count_winning_stars == 1:
    print("Ganhou o 12º Prémio!")
elif count_winning_numbers == 2 and count_winning_stars == 0:
    print("Ganhou o 13º Prémio!")
else:
    print("Sem Prémio :( ")