'''
Passageiros (Clientes)
Cada passageiro será um processo cliente, que possui:

o Chegada ao aeroporto: Os passageiros chegam ao aeroporto de maneira aleatória, a
partir de tempos definidos pelo sistema.

o Prioridade: Cada passageiro terá uma prioridade associada, que pode ser gerada
aleatoriamente ou definida com base em critérios como a classe do bilhete (primeira
classe, classe executiva ou económica) ou o tempo de chegada.

o Aguardando embarque: O passageiro espera até que a sua vez chegue na fila de
embarque, com base na prioridade definida.

'''
from enum import Enum
from multiprocessing import Event
import time
import random


class PriorityLevel(Enum):
    BAIXA = 3     # 35%
    MÉDIA = 3     # 35%
    ALTA = 2      # 20%
    URGENTE = 1   # 10%
    
# PriorityLevel(3)
# print(PriorityLevel.URGENTE.name)
# PriorityLevel.BAIXA.value


class State(Enum):
    NA_FILA = "NA FILA DE EMBARQUE"
    A_EMBARCAR = "A EMBARCAR"
    EMBARCADO = "EMBARCADO"
    DESISTIU = "DESISTIU"

class Client:
    
    def __init__(self, pid : int, name : str, boarding_priority : PriorityLevel, max_waitTime : float, state :  State):
        pass