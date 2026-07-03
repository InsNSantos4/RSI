from Server.airport_server import AirportServer
from Clients.passenger_generator import passenger_generator
from Clients.client import Client
import random
import time
from threading import Thread, Lock

if __name__ == "__main__":
    random.seed()

    server = AirportServer(num_agents=3, num_gates=3)

    # Start dos processos agents
    server.start_agents()

    # Server hread
    server_thread = Thread(target=server.server_loop, daemon=True)
    server_thread.start()

    #Generating passengers
    gen_normal = Thread(target=passenger_generator, args=(server, 10.0, False))
    gen_peak = Thread(target=passenger_generator, args=(server, 10.0, True))

    gen_normal.start()
    gen_peak.start()

    gen_normal.join()
    gen_peak.join()

    # Espera  para esvaziar filas
    time.sleep(10)

    server.stop()
    server_thread.join(timeout=2)

    server.collect_results()
    server.stop_agents()
    server.save_logs("aeroporto_log.txt")

    print("Log gravado em aeroporto_log.txt")