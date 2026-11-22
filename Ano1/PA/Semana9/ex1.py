from datetime import datetime
#from datetime import date
from dataclasses import dataclass

class Pessoa:

    def __init__(self, primeiro_nome : str , ultimo_nome : str, data_nascimento : datetime , morada : str, altura : float):
        self.first_name = primeiro_nome
        self.last_name = ultimo_nome
        self.birthdate = data_nascimento
        self.address = morada
        self.height = altura

    def __str__(self):
        return f"Primeiro Nome: {self.first_name}\nÚltimo Nome: {self.last_name} \nData de Nascimento: {self.birthdate}\nMorada: {self.address}\nAltura: {self.height}m\n"

@dataclass
class Person:
    first_name : str
    last_name : str
    birthdate : datetime
    address : str
    height : float

#código de teste do ex1.py:
if __name__ == "__main__":
    
    pessoa_1 = Pessoa("Rui", "Oliveira", datetime(2000, 5, 17), "Rua 25 abril", 1.90)
    print(pessoa_1)