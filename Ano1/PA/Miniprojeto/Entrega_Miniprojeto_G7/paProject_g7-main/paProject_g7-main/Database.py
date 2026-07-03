from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, delete, select
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from Host import Host
from Admin import Admin
from Test_Collection import Test_Collection


Base = declarative_base()


engine = create_engine("sqlite:///database.db", future=True)


Session = sessionmaker(bind=engine)

# FAZER DIAGRAMA ENTIDADE-RELAÇÃO PARA TER AS TABELAS CORRETAS CONCEPTUALMENTE



# Admin (name, email (PK), password, permission_level)
class Admin_Table(Base):
    __tablename__ = "Admins"

    name = Column(String, unique=True)
    email = Column(String, name="email", primary_key=True, unique=True)
    password = Column(String, name="password", nullable=True, unique=True)
    smtp_server = Column(String, name="server", nullable=True)
    permission_level = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Admin(name={self.name}, email={self.email}, encrypted_password= , permission_level={self.permission_level})"


# Hosts (id (PK), ip, name, permission_level, FK: admin, test)
class Hosts_Table(Base):
    __tablename__ = "Hosts"

    id = Column(
        Integer, name="id", primary_key=True, nullable=False
    )
    ip = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=True)
    permission_level = Column(Integer, nullable=False)

    tests = relationship("Tests_Table", back_populates="host_rel")

    def __repr__(self):
        return f"Hosts(id={self.id}, ip={self.ip}, name={self.name}, permission_level={self.permission_level})"


# Tests_Table (timestamp (PK) , result, host (PK))
class Tests_Table(Base):
    __tablename__ = "Tests"


    timestamp = Column(DateTime, name="timestamp", primary_key=True)
    result = Column(Boolean, nullable=False)
    host = Column(Integer, ForeignKey(Hosts_Table.id), primary_key=True)

    host_rel = relationship("Hosts_Table", back_populates="tests")

    def __str__(self):
        return f"TestPing( host = {self.host}, Timestamp={self.timestamp}, result={self.result})"

    __repr__ = __str__


Base.metadata.create_all(engine)




def create_session():
    global Session
    return Session()





def store_hosts(hosts: list[Host]):


    session = create_session()
 
    for host in hosts:
        try:
            elem = Hosts_Table(
                id=host.id, ip=host.ip, name=host.name, permission_level=host.permission_level
            )
            session.add(elem)
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            print(f"The host with ip '{host.ip}' already exists")
            
    session.close()  

def remove_hosts(hosts: list[Host]):
   
    session = create_session()
    if len(hosts) != 0:
        try:
            for h in hosts:
                host_to_delete = session.get(Hosts_Table, h.id)

                if host_to_delete:
                    session.delete(host_to_delete)
                    session.commit()
                    print(f"Host with ip '{h.ip}' sucessfully removed")
                else:
                    print(f"Host with ip '{h.ip}' not found")
        except Exception as e:
            session.rollback()
            print(f"Error removing host with ip '{h.ip}'")
            print(e)
    else:
        print("Host list was already empty")

    session.close()
    

def get_hosts():

   

    session = create_session()

    hosts = session.execute(select(Hosts_Table)).scalars().all()

    session.close()


    return hosts




def store_tests(tests: list[Test_Collection]):
  
    session = create_session()
    for test in tests:
            for ping in reversed(test.test_metrics):
                try:
                    elem = Tests_Table(host= test.host.id,timestamp=ping.timestamp, result=ping.on)                                        
                    session.add(elem)
                    session.commit()
                except Exception as e:
                    session.rollback()
                    
    session.close()

def remove_tests_ping(host_list_to_del : list[Host]):
   
    session = create_session()

    for host_to_del in host_list_to_del:
        try:
            statement = delete(Tests_Table).where(
                Tests_Table.host == host_to_del.id
                                )        
        
            result = session.execute(statement)
            session.commit()
        
            print(f"{result.rowcount} tests deleted")

        except Exception as e:

            session.rollback()
            print(e)

    session.close()
    

def get_tests_ping():
    

    session = create_session()

    tests = session.execute(select(Tests_Table)).scalars().all()

    session.close()
    

    return tests

def get_tests_host_id(host_id):
    
    session = create_session()

    tests = session.query(Tests_Table).filter(Tests_Table.host == host_id).all()

    session.close()
    

    return tests



def store_admins(admins: list[Admin]):
    

    session = create_session()
    for admin in admins:
        try:
            elem = Admin_Table(
                name=admin.name,
                email=admin.email,
                password=admin.password,
                smtp_server=admin.smtp_server,
                permission_level=admin.permission_level,
            )
            session.add(elem)
            session.commit()
        except:
            session.rollback()
            print(f"The admin with email '{admin.email}' already exists")
    session.close()
    

def remove_admins(admins: list[Admin]):
    
    session = create_session()
    if len(admins) != 0:
        try:
            for admin in admins:
                admin_to_delete = session.get(Admin_Table, admin.email)

                if admin_to_delete:
                    session.delete(admin_to_delete)
                    session.commit()
                    print(f"Admin with email '{admin.email}' sucessfully removed")
                else:
                    print(f"Admin with email '{admin.email}' not found")
        except:
            session.rollback()
            print(f"Error removing admin with email '{admin.email}'")
    else:
        print("Admin list was already empty")

    session.close()
   

def get_admin():
    

    session = create_session()

    admins = session.execute(select(Admin_Table)).scalars().all()

    session.close()
   

    return admins







# Test_CPU (percentage, numCores) || we probably won't be doing this type of test (even if we wanted to try, future upgrades TBD)


# Ao se usar o ficheiro/módulo Database.py no MonitorService,
# abrir lá a Session com o sessionmaker e o engine com o create_engine
# além de ir adicionando, mudando e alterando/atualizando os dados,
# dependendo da função e do seu propósito no MonitorService #

# No entanto, há funções que terão que estar aqui: (ver UML)
