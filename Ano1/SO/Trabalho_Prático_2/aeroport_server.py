'''
Aeroporto (Servidor)
O aeroporto é o "processo servidor", que gere todos os recursos e a comunicação com os
passageiros. As suas funções principais serão:

o Triagem de passageiros: O servidor deve receber a chegada de passageiros,
atribuindo-lhes uma prioridade com base em informações como a classe do bilhete ou
o tempo de chegada.

o Gestão da fila de embarque: O servidor mantém uma fila de passageiros, organizada
por prioridade (alta, média, baixa).

o Atribuição de portões e agentes de embarque: Quando o embarque de um passageiro
é autorizado, o servidor deve alocar um portão disponível e um agente de embarque
para o passageiro.

o Registo de operações: O servidor mantém um registo (log) com a hora de chegada dos
passageiros, a sua prioridade, o tempo de espera e a duração do embarque.

'''

from multiprocessing import Process
import time

# Aeroporto que gere a fila de passageiros
class Server:
    pass