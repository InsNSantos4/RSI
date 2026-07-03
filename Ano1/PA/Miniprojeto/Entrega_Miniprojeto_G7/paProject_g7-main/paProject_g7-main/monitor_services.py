from Host import Host
from Admin import Admin
import Database
import Test_Collection
from Test_Collection import Test_Collection
from Test_file import Test
from Test_file import Ping
import json

class MonitorService:
    def __init__(self):
        self.hosts =    self.innit_list_hosts()      
        self.admins =   self.get_list_admins()     
        self.tests =    self.innit_test()            

    def innit_list_hosts(self):
        
        hosts = Database.get_hosts()
        if hosts:
            temp_host_list = []
            for host in hosts:                   #List from the Database
                
                h =Host(
                    id =    host.id,
                    ip =    host.ip,
                    name =  host.name,
                    permission_level = host.permission_level
                    )
                temp_host_list.append(h)

            return temp_host_list
        else:
            hosts = []
            return hosts




    def add_host(self, id: int, ip : str ,name : str, permission_level : int):
        
        new_host = Host(id, ip, name, permission_level)

        self.hosts.append(new_host)

        testc = Test_Collection(new_host,[])
        self.tests.append(testc)
        host_list = [new_host]
        Database.store_hosts(host_list)

    def remove_host(self, host_list_to_del: list[Host]):
        
        try:
            MonitorService.remove_tests(self,host_list_to_del)
            Database.remove_hosts(host_list_to_del)
        

          
            for host_to_rem in host_list_to_del:
                
                if host_to_rem in self.hosts:
                    self.hosts.remove(host_to_rem)

            return True
        except:
            return False



        return removed

    def read_json_host(entry_file):
        try:
            with open(entry_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return f"Error: File {entry_file} not found"
        except json.JSONDecodeError:
            return f"Error: File not in json format"    



    def get_list_admins(self):
        
        admins = Database.get_admin()
        if admins:
            temp_admin_list = []
            for admin in admins:

                a = Admin(
                    name=admin.name,
                    email=admin.email,
                    password=admin.password,
                    smtp_server=admin.smtp_server,
                    permission_level=admin.permission_level
                )
                temp_admin_list.append(a)

            return temp_admin_list
        else:
            admins = []
            return admins
        
    def add_admin(self, name : str, email : str, password : str, smtp_server : str, permission_level: int):

        new_admin = Admin(name, email, password, smtp_server, permission_level)

        self.admins.append(new_admin)
        
        admin_list = [new_admin]
        Database.store_admins(admin_list)

    def remove_admin(self, email : str):
        try:
            for admin in self.admins:
                if admin.email == email:
                    self.admins.remove(admin)
            
                    Database.remove_admins([admin])
                    return True
        except:
            return False

    def innit_test(self):

        tc_list = []

        if self.hosts == []:
            return tc_list

        for host in self.hosts:
            
            rows = Database.get_tests_host_id(host.id)
            ping_list = []
            for row in rows:
                p = Ping()
                p.timestamp = row.timestamp
                p.on = row.result
                ping_list.append(p)

            tc = Test_Collection(host, ping_list)
            tc_list.append(tc)
        
        return tc_list

    def collect_metrics(self):

        for tc in self.tests:
            Test_Collection.get_metrics(tc)

    def update_Tests_Table(self):

        Database.store_tests(self.tests) #Fazer periodicamente ou como comandop de refresh
                                         #Sempre depois de collect_metrics()

    def remove_tests(self, host_test_list_to_del : list[Host]):

        for host_test_to_del in host_test_list_to_del:

            for tc in self.tests:
                if host_test_to_del.id == tc.host.id:
                    tc.test_metrics = []
        
        Database.remove_tests_ping(host_test_list_to_del)




    def alert_trigger(self):                          #Para ser usado depois de collect_metrics
                                                    
        for tc in self.tests:
            if not tc.test_metrics[-1].on:           #Se o ultimo ping for negativo

                for admin in self.admins:
                    if tc.host.permission_level <= admin.permission_level:
                        Admin.send_email(tc.host.ip)
                           


    def get_status(self, host: Host):
        for tc in self.tests:
            if host.id == tc.host.id:           
                return tc.test_metrics[-1]      #Ultimo Ping



    def get_history(self, ip):

        host = None

        for tc in self.tests:

            if tc.host.ip == ip:
                host = tc    

        timestamps = []
        results = []

        for test in host.test_metrics:

            timestamps.append(test.timestamp)

            if test.on:
                results.append(1)
            else:
                results.append(0)

        return timestamps, results


    def bool_to_str( bool: bool ):
        if bool:
            return "Host ON"
        else:
            return "Host OFF"

    def export_data_all(exit_file):
        data = []
        rows = Database.get_tests_ping()

        for row in rows:
            
            status = MonitorService.bool_to_str(row.result)
            data.append({
                    "Host.id": row.host,
                    "Timestamp": str(row.timestamp),
                    "Machine_Status": status
                        })
        try:
            with open(exit_file,"w", encoding="utf-8") as f:
                json.dump(data,f, indent=4,ensure_ascii=False)
            return True
        except:
            return False

    def export_data_single(host: Host, exit_file):
        
        data = []

        rows = Database.get_tests_host_id(host.id)
        for row in rows:
            
            status = MonitorService.bool_to_str(row.result)
            data.append({
                    "Host.id": row.host,
                    "Timestamp": str(row.timestamp),
                    "Machine_Status": status
                        })
        try:   
            with open(exit_file,"w", encoding="utf-8") as f:
                json.dump(data,f, indent=4,ensure_ascii=False)
            return True
        except:
            return False

    def validate_ip( ip : str ):
        
        parts = ip.split(".") 
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not int(part.isdigit()):
                return False

        if not 0 <= int(part) <= 255:
            return False
        return True
    
    def validate_permission_level(n : int):
        return 1 <= n <= 5
    
    