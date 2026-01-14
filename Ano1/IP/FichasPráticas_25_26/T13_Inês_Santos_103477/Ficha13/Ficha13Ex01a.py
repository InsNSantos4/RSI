# Ficha  Ex 01a

numerador = 10
numerador = 'a'
denominador=0
#result = numerador / denominador
try:
    result = numerador/denominador
except ZeroDivisionError:
    result = 'O denoninador tem que ser diferente de zero'
except TypeError:
    result = ' Os valores têm que ser numericos'
#except:
#   result = ' Ocorreu um erro'


print(result)
