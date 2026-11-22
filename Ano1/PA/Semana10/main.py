from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Departamento(Base):
    __tablename__ = "departamento"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)


    cursos_relationship = relationship("Curso", backref="departament")


    # Python usa __str__ para fazer prints a dados que não são listas
    def __str__(self):
        return f"Departamento(id={self.id}, name={self.name})"
    
    # Bases de dados usam o __repr__ para listar listas/filtros/etc, e redireciona para o __str__:
    def __repr__(self):
        return self.__str__()


class Curso(Base):
    __tablename__ = "curso"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, name="nome")
    descricao = Column(String, nullable=False)
    #departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento_id = Column(Integer, ForeignKey(Departamento.id), nullable=False, )


#create_engine('sqlite:///memory:')

#Se eu quisesse estabelecer uma ligação a uma base de dados remota:
#engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

engine = create_engine('sqlite:///pa_aulaBD.db')

# Criar a estrutura de base de dados, as tabelas:
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
#Criar a sessão (com o session com letra minúscula)
session = Session()



#all = session.query(Departamento).filter_by(name="estga").all()
#fazer __str__, stringificar dados OU __rep__ para listas:
#print(all)

#first = session.query(Departamento).first()
#fazer __str__, stringificar dados OU __rep__ para listas:
#print(first) 


# Criar Departamento estga
estga = session.query(Departamento).filter_by(name="estga").first()
if estga is None:
    estga = Departamento(name="estga")
    session.add(estga)

    # try except no commit, porque os erros acontecem ao fazer commit 
    session.commit()

# Criar Departamento fisica
fisica = session.query(Departamento).filter_by(name="física").first()
if fisica is None:
    fisica = Departamento(name="física")
    session.add(fisica)

    # try except no commit, porque os erros acontecem ao fazer commit 
    session.commit()

print(estga)
print(fisica)


# Criar curso rsi
rsi = Curso(name="RSI", descricao="RSI", departamento_id=estga.id)
session.add(rsi)
session.commit()

fisica = Curso(name="física", descricao="física", departament=Departamento(name="fisica"))      #back reference ao id do Departamento (ir ao Departamento e criar uma relação)

session.close()
engine.dispose()