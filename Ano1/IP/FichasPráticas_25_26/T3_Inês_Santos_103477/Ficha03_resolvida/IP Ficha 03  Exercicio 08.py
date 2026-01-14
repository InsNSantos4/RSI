#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 08
#
# Comissão
# 8. Escreva um programa que permita calcular a comissão que um vendedor obtém na
# venda de uma encomenda cujo valor é introduzido pelo utilizador.
# A comissão do vendedor é 10% do valor da encomenda se o valor da encomenda for
# superior a 500 Euros e 7.5% caso contrário.


print("\n»»»»»» ")
print("»»»»»»  Este programa calcula a comissão do vendedor sobre a venda de uma encomenda")
print("»»»»»»\n ")


# Ler o valor da encomenda
v_encomenda = float(input("Qual o valor da encomenda? : €"))

if v_encomenda > 500 :
    comissao = v_encomenda * 0.1     # Comissão 10%  (10/100 = 0.1)
else:
    comissao = v_encomenda * 0.075   # Comissão 7.5%  (7.5/100 = 0.075)

print("A sua comissão é de  €", comissao)


# fim do programa
