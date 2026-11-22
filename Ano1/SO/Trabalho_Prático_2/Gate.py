
# Dois Portões

class Gate:
    def __init__(self, gate_id: int):
        self.gate_id = gate_id
        self.busy = False

    def __repr__(self):
        return f"<Gate {self.gate_id} busy={self.busy}>"
