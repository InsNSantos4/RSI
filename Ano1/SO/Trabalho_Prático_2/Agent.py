from Gate import Gate

# Dois Agentes/Employees

gate_1 = Gate(1)
gate_2 = Gate(2)

class Agent:

    # agent_list : list[Gate] = []

    def __init__(self, agent_pid: int):
        self.agent_pid = agent_pid
        self.busy = False
        self.assigned_gate = None
        self.gate_list = [gate_1 , gate_2]

    def assign_gate(self):


    def __repr__(self):
        return f"<Agent {self.agent_pid} busy={self.busy} assign_gate={self.assign_gate}>"

