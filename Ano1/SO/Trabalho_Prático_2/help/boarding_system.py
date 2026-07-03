#!/usr/bin/env python3
from multiprocessing import Manager, Lock, Semaphore


def init_shared_resources(num_portoes: int, num_agentes: int):
    """
    Cria e devolve as estruturas partilhadas:
    - fila: lista de clientes
    - logs: lista de dicionários
    - portoes: lista de booleans (True = livre)
    - lock_fila: Lock para proteger a fila
    - sem_agentes: Semaphore para limitar agentes
    """
    manager = Manager()

    fila = manager.list()                 # lista de Client
    logs = manager.list()                 # lista de dict
    portoes = manager.list([True] * num_portoes)

    lock_fila = Lock()
    sem_agentes = Semaphore(num_agentes)

    return fila, logs, portoes, lock_fila, sem_agentes


def obter_portao_livre(portoes):
    """Devolve índice de portão livre ou None se não houver."""
    for i in range(len(portoes)):
        if portoes[i]:
            portoes[i] = False
            return i
    return None
