#pip install -r requirements.txt

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Departamento(Base):
    __tablename__ = "Departamentos"

    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    nome = Column(String)
    
    #Definir a relação entre entidades.
    #Existe uma relação desta tabela (departamento) com o curso.
    #Para o contexto de utilização do Alchemy o atributo "departamento" será criado na class Curso com
    #um objeto do tipo Departamento()
    cursos_relationship = relationship("Curso", backref="departamento") #cursos = relationship(Curso.__name__)

    #Idealmente deveríamos ser genéricos:
    #cursos_relationship = relationship(Curso.__name__, backref="departamento")
    #Mas o python não permite utilizar uma class (neste caso Curso) antes desta ser definida.
    #Temos de fazer manualmente como acima. Se alterar o nome da classe Curso tem de mudar também o nome na relação.

    def __repr__(self):
        return "<dpto nome='%s')>" % (self.nome)

class Curso(Base):
    __tablename__ = "Cursos"

    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    nome = Column(String)
    dpto_id = Column(Integer, ForeignKey(Departamento.id))

    def __repr__(self):
        return "<curso nome='%s' departamento='%s' id=%d)>" % (self.nome, self.departamento, self.dpto_id)


#engine = create_engine("sqlite:///:memory:", echo=False)
engine = create_engine("sqlite:///examplo.db")
Base.metadata.create_all(engine)

#engine = create_engine("sqlite:///examplo.db")

Session = sessionmaker(bind=engine)

# Criar a sessão
session = Session()


#Vamos adicionar 3 Cursos e respetivos departamentos
# de 3 maneiras diferentes.

# Método 1 
# - Criar o Departamento e adicionar
# - Adicionar
# - Fazer o commit para garantir que vai para a db e o objeto Departamento obtem im id
# - Com o id conhecido, addicionar o curso
estga = Departamento(nome="Estga")
session.add(estga)
session.commit()
session.add(Curso(nome="RSI", dpto_id=estga.id))


# Método 2
# - Criar o Departamento e adicionar
# - Associá-lo ao curso e adicionar o curso
# - O id será gerido pela relationship definida na classe Departamento
# - Com o id conhecido, addicionar o curso
deti = Departamento(nome="deti")
session.add(Curso(nome="ET", departamento=deti))
session.add(Curso(nome="CT", departamento=deti))
session.commit()


# Método 2
# - Criar Curso e Departamento juntos e adicionar
session.add(Curso(nome="BIO", departamento=Departamento(nome="dbio")))
#Este método tem o problema. Se executarmos a linha abaixo iremos ter dois departamentos com o mesmo nome e id diferente
#session.add(Curso(nome="BIO2", departamento=Departamento(nome="dbio")))
session.commit()


#Print both tables
print(session.query(Departamento).all())
print(session.query(Curso).all())


#Na realidade devemos sempre verificar se o departamento já existe
#Imagine que já temos uma tabela com elementos e alguns departamentos criados,
#queremos adicionar o curso PSI da estga, mas não temos a certeza de se a estga já existe
estga = session.query(Departamento).filter(Departamento.nome=="Estga").first()
if estga is None: 
    estga = Departamento(nome="Estga")
session.add(Curso(nome="PSI", departamento=estga))

fisica = session.query(Departamento).filter(Departamento.nome=="dfis").first()
if fisica is None: fisica = Departamento(nome="dfis")
session.add(Curso(nome="EF", departamento=fisica))

session.commit()

#Print both tables
print(session.query(Departamento).all())
print(session.query(Curso).all())

session.close()
engine.dispose()