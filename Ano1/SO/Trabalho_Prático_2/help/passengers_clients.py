#!/usr/bin/env python3
from enum import Enum
from multiprocessing import Event
import time
import random


class PriorityLevel(Enum):
    BAIXA = 3     # menor prioridade
    MEDIA = 3
    ALTA = 2
    URGENTE = 1   # maior prioridade


class State(Enum):
    NA_FILA = "NA FILA DE EMBARQUE"
    A_EMBARCAR = "A EMBARCAR"
    EMBARCADO = "EMBARCADO"
    DESISTIU = "DESISTIU"


class Client:
    def __init__(
        self,
        pid: int,
        name: str,
        boarding_priority: PriorityLevel,
        max_waitTime: float,
        state: State = State.NA_FILA,
    ):
        self.pid = pid
        self.name = name
        self.priority = boarding_priority
        self.max_wait = max_waitTime
        self.state = state

        self.event = Event()
        self.arrival_time = time.time()

    def wait_for_boarding(self, logs):
        """Espera autorização do servidor até max_wait; se não, desiste."""
        autorizado = self.event.wait(self.max_wait)

        if not autorizado:
            self.state = State.DESISTIU
            logs.append({
                "id": self.pid,
                "nome": self.name,
                "prioridade": self.priority.name,
                "estado": self.state.value,
                "tempo_espera": self.max_wait,
                "duracao_embarque": 0.0,
                "desistiu": True,
                "portao": None,
            })
            return False

        return True

    def board(self, logs, gate_id: int | None = None):
        """Simula o embarque do passageiro e regista tempos."""
        self.state = State.A_EMBARCAR
        inicio = time.time()
        duracao = random.uniform(1, 3)
        time.sleep(duracao)
        fim = time.time()
        self.state = State.EMBARCADO

        logs.append({
            "id": self.pid,
            "nome": self.name,
            "prioridade": self.priority.name,
            "estado": self.state.value,
            "tempo_espera": inicio - self.arrival_time,
            "duracao_embarque": duracao,
            "desistiu": False,
            "portao": gate_id,
            "inicio_embarque": inicio,
            "fim_embarque": fim,
        })
