# Ficha  Ex 01

numerador = 10
denominador=0
lista=['aula IP']
#result = numerador / denominador

try:
    print(lista[0])
    #print(lista[1])
    result = numerador / denominador
    print(result)
except ZeroDivisionError:
     print(' Ocorreu um erro divisão por Zero')
except NameError:
     print('Variavel não definida')
except:
    print('Ocorreu um erro')


#else:
print('continua o programa')
