from num2words import num2words

class Celsius:
    def __init__(self, valor=0):
        #self.setTemperatura(valor)
        self.temperatura = valor
    
    # @ -> anotações/funções executadas dentro da função // função que modifica o código da função internamente
    #intermediário para o setter e o getter; "atributo virtual"
    #@property
    def getTemperatura(self):
        return self.__temperatura
    
    #@temperatura.setter
    def setTemperatura(self, nova_temp):
        if nova_temp < - 273.15:
            self.__temperatura =  - 273.15
        else:
            self.__temperatura = nova_temp
    
    temperatura = property(getTemperatura, setTemperatura)
    
    # método de instância
    def to_fahrenheit(self):
        return (self.__temperatura * 1.8) + 32
    
    def extenso(self):
        return f"{num2words(self.temperatura, lang='pt_BR').capitalize()} {self.__grauString()}"
    
    def __grauString(self):
        if( self.temperatura == 1 or self.temperatura == -1 ):
            return "grau Celsius"
        else: return "graus Celsius"

'''
    celsius1 = Celsius(13)

    #print(f"Temperatura atual em graus Celsius: {celsius1.temperatura}")
    #print(f"Temperatura atual em graus Fahrenheit: {celsius1.to_fahrenheit():.2f}\n")

    def soma(lista : list[Celsius]) -> Celsius: # retorna um objeto Celsius
        sum=Celsius(0)    
        for t in lista:
            sum.temperatura += t.temperatura
        return sum


    c1 = Celsius(15)
    c2 = Celsius(20)
    c3 = Celsius(25)
    c4 = Celsius(30)
    c5 = Celsius(35)

    temps = [c1, c2, c3, c4, c5]

    def media(temperaturas : list[Celsius]) -> Celsius:    
        return soma(temperaturas).temperatura / (len(temperaturas))

    #print(f"Somatório das temperaturas dos elementos de uma lista de Celsius : {soma(temps).temperatura} graus")
    #print(f"Média de valores da lista de temperaturas em Celsius : {media(temps)} graus")

'''