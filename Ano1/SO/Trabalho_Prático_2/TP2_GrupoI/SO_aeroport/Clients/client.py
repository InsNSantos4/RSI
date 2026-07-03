import time
import random
from Server.state import State

class Client:
    next_pid = 1

    def __init__(self):
        self.pid = Client.next_pid
        Client.next_pid += 1

        self.ticket_class = self.define_ticket_class()
        self.prio = self.define_prio()

        self.arrival_time = time.time()
        self.boarding_start_time = None
        self.boarding_end_time = None

        self.waiting_time = 0

        
        self.TTL = self.define_ttl()
        self.gave_up = False

        self.state = State.IN_QUEUE

    def define_ticket_class(self):  #Ticket class por percentagens
        return random.choices(
            ["first", "business", "economy"],
            weights=[10, 20, 70],
            k=1
        )[0]

    def define_prio(self):              #Assigna a prio com base no ticket class
        if self.ticket_class == "first":
            return 1
        elif self.ticket_class == "business":
            return 2
        return 3

    def define_ttl(self):
                                                    # prioridade alta --> menos paciente
        match self.prio:
            case 1:
                return random.randint(3, 7)
            case 2:
                return random.randint(7, 12)
            case 3:
                return random.randint(12, 18)

    def __repr__(self):
        return f"<Client pid={self.pid} class={self.ticket_class} prio={self.prio} state={self.state.value}>"
