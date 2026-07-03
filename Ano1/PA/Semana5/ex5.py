from Celsius import Celsius
#from num2words import num2words

def soma(lista : list[Celsius]) -> Celsius: # retorna um objeto Celsius
    sum=Celsius(0)    
    for t in lista:
        #sum.temperatura += t.temperatura
        sum.setTemperatura(sum.getTemperatura() + t.getTemperatura())
    return sum

c1 = Celsius(15)
c2 = Celsius(20)
c3 = Celsius(25)
c4 = Celsius(30)

temps = [c1, c2, c3, c4, Celsius(35)]

def media(temperaturas : list[Celsius]) -> Celsius:    
    return soma(temperaturas).temperatura / (len(temperaturas))

print(f"\nSomatório das temperaturas dos elementos de uma lista de Celsius : {soma(temps).temperatura} graus")
print(f"Média de valores da lista de temperaturas em Celsius : {media(temps)} graus \n")


print(c1.extenso()) 
c2.setTemperatura(-2)
print(c2.extenso())

c3.setTemperatura(-1)
print(c3.extenso())
c4.setTemperatura(1)
print(c4.extenso())

print(c2.extenso())
print(Celsius(-4).extenso())