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

    def __add__(self, other_Celsius):
        return Celsius(self.temperatura + other_Celsius.temperatura)


def soma(lista : list[Celsius]) -> Celsius: # retorna um objeto Celsius
    sum=Celsius(0)    
    for t in lista:
        sum.temperatura += t.temperatura
    return sum

def media(temperaturas : list[Celsius]) -> Celsius:    
    return soma(temperaturas).temperatura / (len(temperaturas))