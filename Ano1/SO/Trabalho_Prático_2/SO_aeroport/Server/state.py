from enum import Enum

class State(Enum):
    IN_QUEUE = "IN QUEUE"
    BOARDING = "BOARDING"
    BOARDED = "BOARDED"
    GAVE_UP = "GAVE UP"
