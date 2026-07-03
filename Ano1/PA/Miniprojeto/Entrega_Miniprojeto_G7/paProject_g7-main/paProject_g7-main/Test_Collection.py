import Test_file
from Test_file import Test
from Test_file import Ping
import Host


class Test_Collection:

    def __init__(self,host : Host, test_metrics : list[Ping]):

        self.host = host
        self.test_metrics = test_metrics  or []          


    def __str__(self):
        return f"{self.host} {self.test_metrics}" 

    def get_metrics(self):
        
        p = Ping()
        Ping.metrics_scraper(p,self.host)
        self.test_metrics.append(p)
