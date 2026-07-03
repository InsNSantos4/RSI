#!/usr/bin/env python3
"""
Sistema de embarque concorrente com:
- 1 servidor (aeroporto)
- N passageiros (clientes)
- memória partilhada + semáforos + locks
"""

import time
import random
from multiprocessing import Process, Event

from shared_memory import init_shared_resources, obter_portao_livre
from passengers_clients import Client, PriorityLevel


NUM_PASSAGEIROS = 20
NUM_PORTOES = 3
NUM_AGENTES = 2
CHEGADA_MIN = 0.1
CHEGADA_MAX = 1.0
MAX_WAIT_MIN = 5.0
MAX_WAIT_MAX = 15.0


def servidor_proc(fila, logs, portoes, lock_fila, sem_agentes, stop_event):
    """
    Processo servidor:
    - escolhe próximo cliente por prioridade + chegada
    - aloca agente + portão
    - autoriza embarque via Event
    - liberta recursos após tempo máximo de embarque
    """
    while True:
        if stop_event.is_set():
            with lock_fila:
                if not fila:
                    break

        with lock_fila:
            if not fila:
                time.sleep(0.1)
                continue

            fila.sort(key=lambda c: (c.priority.value, c.arrival_time))
            client = fila.pop(0)

        sem_agentes.acquire()

        gate_id = obter_portao_livre(portoes)
        if gate_id is None:
            sem_agentes.release()
            time.sleep(0.1)
            continue

        client.event.set()

        def libertar_recursos(gid: int, cid: int):
            time.sleep(4)
            portoes[gid] = True
            sem_agentes.release()

        Process(target=libertar_recursos, args=(gate_id, client.pid), daemon=True).start()


def passageiro_main(client: Client, fila, logs, lock_fila):
    """Função do processo passageiro."""
    with lock_fila:
        fila.append(client)

    if client.wait_for_boarding(logs):
        client.board(logs)


def main():
    random.seed()

    fila, logs, portoes, lock_fila, sem_agentes = init_shared_resources(
        NUM_PORTOES, NUM_AGENTES
    )

    stop_event = Event()

    servidor = Process(
        target=servidor_proc,
        args=(fila, logs, portoes, lock_fila, sem_agentes, stop_event),
        name="Servidor",
    )
    servidor.start()

    passageiros = []
    for pid in range(NUM_PASSAGEIROS):
        prio = random.choice(list(PriorityLevel))
        max_wait = random.uniform(MAX_WAIT_MIN, MAX_WAIT_MAX)
        client = Client(
            pid=pid,
            name=f"Passageiro-{pid}",
            boarding_priority=prio,
            max_waitTime=max_wait,
        )

        p = Process(
            target=passageiro_main,
            args=(client, fila, logs, lock_fila),
            name=f"Passageiro-{pid}",
        )
        p.start()
        passageiros.append(p)

        time.sleep(random.uniform(CHEGADA_MIN, CHEGADA_MAX))

    for p in passageiros:
        p.join()

    stop_event.set()
    servidor.join()

    print("\n=== LOG FINAL ===")
    for entry in list(logs):
        print(entry)


if __name__ == "__main__":
    main()
