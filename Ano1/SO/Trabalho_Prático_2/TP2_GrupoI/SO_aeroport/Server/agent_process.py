import time
import random
from multiprocessing import Process, Queue
from Server.state import State
from Server.gate import Gate
from Clients.client import Client
from queue import PriorityQueue


class AgentProcess(Process):
    def __init__(self, agent_id, gates, task_queue: Queue, result_queue: Queue):
        super().__init__()
        self.agent_id = agent_id
        self.gates = gates         
        self.task_queue = task_queue
        self.result_queue = result_queue

    def assign_gate(self):
        
        for gate in self.gates:
            if not gate["busy"]:
                gate["busy"] = True
                return gate["id"]
        return None

    def release_gate(self, gate_id):
        for gate in self.gates:
            if gate["id"] == gate_id:
                gate["busy"] = False
                return

    def get_boarding_time(self, client: Client) -> float:
        

        if client.prio == 1:
            return random.uniform(1.0, 2.0)
        elif client.prio == 2:
            return random.uniform(2.0, 3.0)
        else:
            return random.uniform(3.0, 4.0)

    def run(self):
        while True:
            client = self.task_queue.get()
            if client is None:
                                                #Stops running se for none
                break

            
            gate_id = None                       #Atribuir Gate
            while gate_id is None:
                gate_id = self.assign_gate()
                if gate_id is None:
                    time.sleep(0.1)

            start = time.time()
            wait_time = start - client.arrival_time

            
            boarding_time = self.get_boarding_time(client)      #Simular tempo de embarque
            time.sleep(boarding_time)
            end = time.time()

           
            self.release_gate(gate_id)

                                                    #Envia resultado para o servidor
            self.result_queue.put({
                "client_pid": client.pid,
                "agent_id": self.agent_id,
                "gate_id": gate_id,
                "prio": client.prio,
                "wait_time": wait_time,
                "boarding_duration": end - start,
                "arrival_time": client.arrival_time,
                "boarding_start": start,
                "boarding_end": end,
            })
