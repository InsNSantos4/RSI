#
# POP outubro 2022
#
# Avisos Meteorológicos
# 4.	O Instituto Português do Mar e da Atmosfera (IPMA) define 3 avisos meteorológicos: Amarelo, Laranja e Vermelho.
# Existem vários critérios que podem levar à emissão desses avisos meteorológicos:
#     vento, precipitação, tempo quente, tempo frio e agitação marítima.
#     Um aviso vermelho, por exemplo, pode dever-se a rajadas de vento muito fortes ou a temperaturas elevadas.
# Desenvolva um programa que, face aos valores introduzidos para cada critério,
# apresente o respetivo aviso meteorológico (caso exista). Considere a seguinte tabela:
#
# Aviso	Amarelo	Laranja	Vermelho	Unidade
# Vento	70 – 90	91 – 130	> 130	Km/h
# Precipitação	10 – 20	21 – 40	> 40	Mm/h
# Tempo quente	32 – 36	37 – 38	> 38	ºC
# Tempo frio	1 – (-1)	(-2) – (-3)	< (-3)	ºC
# Agitação marítima	4 – 5	6 – 7	> 7	m
#
# Na saída deve ser indicado o tipo de aviso, discriminando-se o(s) critérios(s) que fizeram
# com que existisse(m) o(s) aviso(s). Se não existir qualquer aviso deve surgir na saída a
# mensagem “Sem qualquer aviso”.


print("\n»»»»»» ")
print("»»»»»»  Este programa lê as previsões dos dados metereológicos")
print("»»»»»»   e retorna se há lugar a aviso(s) meterológico(s) e qual/quais")
print("»»»»»»\n ")
print("\n")

# Entrada de dados
vento = int(input("Entre a velocidade do vento (Km/h): "))
precipitacao = int(input("Entre a precipitação (mm/h): "))
temperatura = int(input("Entre a temperatura (ºC): "))
agit_mar = int(input("Entre a agitação marítima (m): "))
print("\n")
# »»»»»»»»»»»»»»»»»  Verificação aviso Vento
if vento < 70:  # sem aviso
    vento_aviso = False
    vento_msg = ''
    vento_gravidade = 0
elif 70 <= vento <= 90:  # Aviso Amarelo
    vento_aviso = True
    vento_msg = str(' Vento:             Aviso Amarelo ' + str(vento) + 'Km/h   (70 a 90 Km/h)')
    vento_gravidade = 1
elif 91 <= vento <= 130:  # Aviso Laranja
    vento_aviso = True
    vento_msg = str(' Vento:             Aviso Laranja ' + str(vento) + 'Km/h   (90 a 130 Km/h)')
    vento_gravidade = 2
elif 130 < vento:  # Aviso Vermelho
    vento_aviso = True
    vento_msg = str(' Vento:             Aviso Vermelho ' + str(vento) + 'Km/h  (superior a 130 Km/h)')
    vento_gravidade = 3

# »»»»»»»»»»»»»»»»»  Verificação aviso Precipitação
if precipitacao < 10:  # sem aviso
    precipitacao_aviso = False
    precipitacao_msg = ''
    precipitacao_gravidade = 0
elif 10 <= precipitacao <= 20:  # Aviso Amarelo
    precipitacao_aviso = True
    precipitacao_msg = str(' Precipitação:      Aviso Amarelo ' + str(precipitacao) + 'mm/h   (10 a 20mm/h)')
    precipitacao_gravidade = 1
elif 21 <= precipitacao <= 40:  # Aviso Laranja
    precipitacao_aviso = True
    precipitacao_msg = str(' Precipitação:      Aviso Laranja ' + str(precipitacao) + 'mm/h   (21 a 40mm/h)')
    precipitacao_gravidade = 2
elif 40 < precipitacao:  # Aviso Vermelho
    precipitacao_aviso = True
    precipitacao_msg = str(' Precipitação:      Aviso Vermelho ' + str(precipitacao) + 'mm/h   (superior a 40mm/h)')
    precipitacao_gravidade = 3

# »»»»»»»»»»»»»»»»»  Verificação aviso Agitação Maritima
if agit_mar < 4:  # sem aviso
    agit_mar_aviso = False
    agit_mar_msg = ''
    agit_mar_gravidade = 0
elif 4 <= agit_mar <= 5:  # Aviso Amarelo
    agit_mar_aviso = True
    agit_mar_msg = str(' Agitação Maritima: Aviso Amarelo ' + str(agit_mar) + 'm   (4 a 5m)')
    agit_mar_gravidade = 1
elif 6 <= agit_mar <= 7:  # Aviso Laranja
    agit_mar_aviso = True
    agit_mar_msg = str(' Agitação Maritima: Aviso Laranja ' + str(agit_mar) + 'm   (6 a 7m)')
    agit_mar_gravidade = 2
elif 7 < agit_mar:  # Aviso Vermelho
    agit_mar_aviso = True
    agit_mar_msg = str(' Agitação Maritima: Aviso Vermelho ' + str(agit_mar) + 'm   (superior a 7m)')
    agit_mar_gravidade = 3

# »»»»»»»»»»»»»»»»»  Verificação aviso Temperatura
if 1 < temperatura < 32:  # sem aviso
    temperatura_aviso = False
    temperatura_msg = ''
    temperatura_gravidade = 0
elif 32 <= temperatura <= 36:  # Aviso Amarelo Tempo Quente
    temperatura_aviso = True
    temperatura_msg = str(' Temperatura:       Aviso Amarelo Tempo Quente ' + str(temperatura) + 'ºC  (32 a 36ºC)')
    temperatura_gravidade = 1
elif 37 <= temperatura <= 38:  # Aviso Laranja Tempo Quente
    temperatura_aviso = True
    temperatura_msg = str(' Temperatura:       Aviso Laranja Tempo Quente ' + str(temperatura) + 'ºC  (36 a 38ºC)')
    temperatura_gravidade = 2
elif 38 < temperatura:  # Aviso Vermelho Tempo Quente
    temperatura_aviso = True
    temperatura_msg = str(
        ' Temperatura:       Aviso Vermelho Tempo Quente ' + str(temperatura) + 'ºC (superior a 38ºC)')
    temperatura_gravidade = 3

elif -1 <= temperatura <= 1:  # Aviso Amarelo Tempo Frio
    temperatura_aviso = True
    temperatura_msg = str(' Temperatura:       Aviso Amarelo Tempo Frio ' + str(temperatura) + 'ºC  (-1 a 1ºC)')
    temperatura_gravidade = 1
elif -2 <= temperatura <= -3:  # Aviso Laranja Tempo Frio
    temperatura_aviso = True
    temperatura_msg = str(' Temperatura:       Aviso Laranja Tempo Frio ' + str(temperatura) + 'ºC  (-2 a -3ºC)')
    temperatura_gravidade = 2
elif -3 > temperatura:  # Aviso Vermelho Tempo Frio
    temperatura_aviso = True
    temperatura_msg = str(' Temperatura:       Aviso Vermelho Tempo Frio ' + str(temperatura) + 'ºC (inferior a -3ºC)')
    temperatura_gravidade = 3

#  Avisos
if not (temperatura_aviso or agit_mar_aviso or vento_aviso or precipitacao_aviso):  # sem avisos
    print(" Sem qualquer Aviso Meterológico")
else:
    aviso = 0

    # Aviso Vermelho
    if (temperatura_gravidade == 3) or (agit_mar_gravidade == 3) \
            or (precipitacao_gravidade == 3) or (vento_gravidade == 3):
        aviso = 3
        print("AVISO VERMELHO: ")
        if temperatura_gravidade == 3:
            print(temperatura_msg)
        if agit_mar_gravidade == 3:
            print(agit_mar_msg)
        if precipitacao_gravidade == 3:
            print(precipitacao_msg)
        if vento_gravidade == 3:
            print(vento_msg)

    # Aviso Laranja
    if (temperatura_gravidade == 2) or (agit_mar_gravidade == 2) \
            or (precipitacao_gravidade == 2) or (vento_gravidade == 2):
        if aviso == 0:
            aviso = 2
            print("AVISO LARANJA: ")
        if temperatura_gravidade == 2:
            print(temperatura_msg)
        if agit_mar_gravidade == 2:
            print(agit_mar_msg)
        if precipitacao_gravidade == 2:
            print(precipitacao_msg)
        if vento_gravidade == 2:
            print(vento_msg)

    # Aviso Amarelo
    if (temperatura_gravidade == 1) or (agit_mar_gravidade == 1) \
            or (precipitacao_gravidade == 1) or (vento_gravidade == 1):
        if aviso == 0:
            aviso = 1
            print("AVISO AMARELO: ")
        if (temperatura_gravidade == 1):
            print(temperatura_msg)
        if (agit_mar_gravidade == 1):
            print(agit_mar_msg)
        if (precipitacao_gravidade == 1):
            print(precipitacao_msg)
        if (vento_gravidade == 1):
            print(vento_msg)

# fim do programa
