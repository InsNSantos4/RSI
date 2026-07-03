import time
import random
from Server.airport_server import AirportServer
from Clients.client import Client

def passenger_generator(server: AirportServer, duration: float, high_demand=False):
    start = time.time()
    while time.time() - start < duration:
        client = Client()
        server.add_client(client)

        if high_demand:
            time.sleep(random.uniform(0.1, 0.4))
        else:
            time.sleep(random.uniform(0.5, 1.5))
