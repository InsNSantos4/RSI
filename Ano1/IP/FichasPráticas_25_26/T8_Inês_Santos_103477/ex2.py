# Uma empresa paga aos seus 10 vendedores com base em comissões. O vendedor recebe
# 200€ por semana mais 9% das mesmas vendas por semana.
# Por exemplo, um vendedor que teve vendas no valor de 3000€ numa semana recebe
# 200€ mais 9% de 3000€, ou seja, um total de 470€. Escreva um programa que peça ao
# utilizador uma lista dos/com os valores das vendas dos vendedores e os classifique numa escala
# de 1-9 (1-péssimo vendedor;...; 9-excelente vendedor) de acordo com os seguintes
# intervalos de valores de vendas:
# 1: 200 - 299€
# 2: 300 - 399€
# 3: 400 - 499€
# 4: 500 - 599€
# 5: 600 - 699€
# 6: 700 - 799€
# 7: 800 - 899€
# 8: 900 - 999€
# 9: >=1000€

lista_vendas = []

#Lista com os valores das vendas dos 10 vendedores da empresa:
for i in range(10):
    venda = float(input(f"Valor da venda do vendedor {i+1}: "))
    total_recebido = 200 + 0.09 * venda
    lista_vendas.append(total_recebido)

    if lista_vendas[i] >= 200 and lista_vendas[i] <= 299:
        print(f"1 - O vendedor {i+1} é um péssimo vendedor.")
    elif lista_vendas[i] >= 300 and lista_vendas[i] <= 399:
        print(f"2 - O vendedor {i+1} é muito mau vendedor.")
    elif lista_vendas[i] >= 400 and lista_vendas[i] <= 499:
        print(f"3 - O vendedor {i+1} é um mau vendedor.")
    elif lista_vendas[i] >= 500 and lista_vendas[i] <= 599:
        print(f"4 - O vendedor {i+1} é um mediano vendedor.")
    elif lista_vendas[i] >= 600 and lista_vendas[i] <= 699:
        print(f"5 - O vendedor {i+1} é um razoável vendedor.")
    elif lista_vendas[i] >= 700 and lista_vendas[i] <= 799:
        print(f"6 - O vendedor {i+1} é um bom vendedor.")
    elif lista_vendas[i] >= 800 and lista_vendas[i] <= 899:
        print(f"7 - O vendedor {i+1} é um muito bom vendedor.")
    elif lista_vendas[i] >= 900 and lista_vendas[i] <= 999:
        print(f"8 - O vendedor {i+1} é um ótimo vendedor.")
    elif lista_vendas[i] >= 1000:
        print(f"9 - O vendedor {i+1} é um excelente vendedor.")
    else:
        print(f"0 - O vendedor {i+1} é um horrível vendedor.")