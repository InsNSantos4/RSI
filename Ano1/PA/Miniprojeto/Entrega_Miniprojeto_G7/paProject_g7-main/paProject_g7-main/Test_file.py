#import main
from abc import ABC, abstractmethod
from datetime import datetime
import os
import Host

class Test(ABC):

    def __init__(self):

        self.timestamp = None

    @abstractmethod
    def metrics_scraper(host : Host): ...       #Cada filho vai usar um metrics_scraper diferente



class Ping(Test):

    def __init__(self):
        super().__init__()
        self.on = False

    def __str__(self):
        return f"{self.timestamp} {self.on}"

    def metrics_scraper(self, host : Host):

        self.timestamp = datetime.now()
        
        result = os.system(f"ping -c 1 -W 1 {host.ip} > /dev/null 2>&1")
        if result == 0:
            self.on = True
        
