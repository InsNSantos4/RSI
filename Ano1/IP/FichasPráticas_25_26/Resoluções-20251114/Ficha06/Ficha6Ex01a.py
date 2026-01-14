# Ficha 6 Ex 01
# pop

# Contagem de Votos

while True:
    Jurados = input('Introduza o nº de Jurados da votação (01 a 20): ')
    if Jurados.isdigit():
        J= int(Jurados)
        if 1 <= J <= 20:
            break
    print('!!Valor inválido. INTRODUZA um valor correcto!!')

votosA = 0
votosB = 0
nulos = 0

for i in range(1,J+1):
    voto = input(f'Introduza o voto do jurado nº {i} (A ou B): ')
    if voto =="a" or voto =="A":
        votosA += 1
    elif voto =="b" or voto =="B":
        votosB += 1
    else:
        nulos += 1
        print('!!Valor inválido. Voto considerado NULO!!')

if votosA > votosB:
    print(f"\nVenceu o cantor  A: ")
elif votosA < votosB:
    print(f"\nVenceu o cantor  B: ")
else:
    print(f"\nEmpate: ")

print( "Votação:"
       f"\n Votos A: {votosA}"
       f"\n Votos B: {votosB} "
       f"\n Votos nulos: {nulos} ")