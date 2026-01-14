# Comissão
# 8. Escreva um programa que permita calcular a comissão que um vendedor obtém na
# venda de uma encomenda cujo valor é introduzido pelo utilizador.
# A comissão do vendedor é 10% do valor da encomenda se o valor da encomenda for
# superior a 500 Euros e 7.5% caso contrário.

valor_encomenda = float(input("Introduza o valor da encomenda: "))

if(valor_encomenda > 500):
    comissao_vendedor = 0.1 * valor_encomenda
else:
    comissao_vendedor = 0.075 * valor_encomenda

print("Comissao recebida pelo vendedor: " + str(comissao_vendedor))