import time
from queue import PriorityQueue
from threading import Lock
from multiprocessing import Manager, Queue

from Server.agent_process import AgentProcess
from Server.gate import Gate
from Server.state import State

from Clients.client import Client


class AirportServer:
    def __init__(self, num_agents=3, num_gates=2):
        self.manager = Manager()

        
        self.gates = self.manager.list(     #creating shared gates
            [{"id": i + 1, "busy": False} for i in range(num_gates)]
        )

        
        self.task_queue = Queue()       #taks para os agents/processos
       
        self.result_queue = Queue()     #Resultados dos agentes

        
        self.queue = PriorityQueue()    #creating shared queue
        self.queue_lock = Lock()

        
        self.logs = []                  #Saving logs
        self.logs_lock = Lock()

        
        self.agents: list[AgentProcess] = [                                 #Creating lista de processos/agents
            AgentProcess(i + 1, self.gates, self.task_queue, self.result_queue)
            for i in range(num_agents)
        ]

        self.running = True

    def start_agents(self):
        for ag in self.agents:          #O start ativa o run da processo
            ag.start()

    def stop_agents(self):
        
        for _ in self.agents:
            self.task_queue.put(None)
        for ag in self.agents:
            ag.join()

    def add_client(self, client: Client):                   #Envia para a fila
        with self.queue_lock:
            self.queue.put((client.prio, client.arrival_time, client))
        self.log(f"ARRIVAL: client={client.pid} class={client.ticket_class} prio={client.prio} TTL={client.TTL}s")
        print(f"ARRIVAL: client={client.pid} class={client.ticket_class} prio={client.prio} TTL={client.TTL}s")

    def log(self, msg: str):                #Transforma time em str e guarda logs na lista com a msg dada por cada funcao
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        line = f"[{timestamp}] {msg}"
        with self.logs_lock:
            self.logs.append(line)
        print(line)

    def check_timeouts(self):              #Verifica se desistiram, esvaziando e enchendo a filade novo
        
        with self.queue_lock:
            temp = []
            now = time.time()
            while not self.queue.empty():
                prio, arr, client = self.queue.get()
                if now - client.arrival_time > client.TTL:
                    client.state = State.GAVE_UP
                    client.gave_up = True
                    self.log(
                        f"GAVE UP: client={client.pid} prio={client.prio} "
                        f"waited={now - client.arrival_time:.2f}s TTL={client.TTL}s"
                    )
                    print(f"GAVE UP: client={client.pid} prio={client.prio} ")
                    print(f"waited={now - client.arrival_time:.2f}s TTL={client.TTL}s")
                    
                else:
                    temp.append((prio, arr, client))
            for item in temp:
                self.queue.put(item)

    def dispatch_clients(self):
                                    #Vai buscar clientes e envia para a tas_queue a espera de processos disponiveis
        with self.queue_lock:
            if self.queue.empty():      #Se estiver vazia retorna nada
                return                  
                                            # Vai buscar  um cliente (o de maior prioridade / mais antigo)
            prio, arr, client = self.queue.get()
        
        self.task_queue.put(client)
        self.log(f"DISPATCH: client={client.pid} prio={client.prio} enviado para agentes")
        print(f"DISPATCH: client={client.pid} prio={client.prio} enviado para agentes")

    def collect_results(self):
                            # Recolhe resultados dos agentes e regista logs
        while True:
            try:
                result = self.result_queue.get_nowait()     #Vai buscar
            except Exception:
                break
            self.log(
                f"BOARDED: client={result['client_pid']} prio={result['prio']} "
                f"agent={result['agent_id']} gate={result['gate_id']} "
                f"wait={result['wait_time']:.2f}s duration={result['boarding_duration']:.2f}s"
            )
            print(
                f"BOARDED: client={result['client_pid']} prio={result['prio']} "
                f"agent={result['agent_id']} gate={result['gate_id']} "
                f"wait={result['wait_time']:.2f}s duration={result['boarding_duration']:.2f}s"
            )

    def server_loop(self):
        while self.running:
            
            self.check_timeouts()       #Verifica quem desistiu


            self.dispatch_clients()     #Envia para os agents

            
            self.collect_results()      #Vai buscar os resultados

            time.sleep(0.1)

    def stop(self):
        self.running = False

    def save_logs(self, filename="aeroporto_log.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            with self.logs_lock:
                for line in self.logs:
                    f.write(line + "\n")
