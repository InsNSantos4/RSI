from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Date, Table
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

Base = declarative_base()


# Tabela Departamento (classe)

class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)

    cursos = relationship("Curso", back_populates="departamento")

    # Python usa __str__ para fazer prints a dados que não são listas
    def __str__(self):
        return f"Departamento(id={self.id}, nome={self.nome})"

    # Bases de dados usam o __repr__ para listar listas/filtros/etc, e redireciona para o __str__:
    #__repr__ = __str__      # é a mesma coisa que:
    def __repr__(self):
        return self.__str__()


# Tabela Curso

class Curso(Base):
    __tablename__ = "curso"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento", back_populates="cursos")

    disciplinas = relationship("Disciplina", secondary="curso_disciplina", back_populates="cursos")

    def __str__(self):
        return f"Curso(id={self.id}, nome={self.nome}, departamento={self.departamento.nome})"

    __repr__ = __str__


# Tabela Disciplina

class Disciplina(Base):
    __tablename__ = "disciplina"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_uc = Column(String, nullable=False)

    cursos = relationship("CursoDisciplina", back_populates="disciplina")

    alunos = relationship("Aluno", secondary="inscrito", back_populates="disciplinas")

    def __str__(self):
        return f"Disciplina(id={self.id}, nome_uc={self.nome_uc})"

    __repr__ = __str__


# Tabela associativa da Relação DisciplinaCurso (N‑M): Curso — Disciplina

class CursoDisciplina(Base):
    __tablename__ = "curso_disciplina"

    curso_id = Column(Integer, ForeignKey("curso.id"), primary_key=True)
    disciplina_id = Column(Integer, ForeignKey("disciplina.id"), primary_key=True)

    id = Column(Integer, primary_key=True, autoincrement=True)
    ano = Column(Integer, nullable=False)
    semestre = Column(Integer, nullable=False)

    curso = relationship("Curso", back_populates="disciplinas")
    disciplina = relationship("Disciplina", back_populates="cursos")

    def __str__(self):
        return f"CursoDisciplina(curso={self.curso_id}, disciplina={self.disciplina_id}, ano={self.ano}, semestre={self.semestre})"

    __repr__ = __str__


# Tabela Aluno

class Aluno(Base):
    __tablename__ = "aluno"

    nmec = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    morada = Column(String, nullable=False)

    disciplinas = relationship("Disciplina", secondary="inscrito", back_populates="alunos")

    def __str__(self):
        return f"Aluno(nmec={self.nmec}, nome={self.nome})"

    __repr__ = __str__


#Tabela da relação DisciplinaAluno (N-M): Inscrito

Inscrito = Table(
    "inscrito",
    Base.metadata,
    Column("aluno_id", Integer, ForeignKey("aluno.nmec"), primary_key=True),
    Column("disciplina_id", Integer, ForeignKey("disciplina.id"), primary_key=True)
)




# Criar a estrutura de base de dados, as tabelas:

engine = create_engine("sqlite:///info_universidade.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
#Criar a sessão (com o session com letra minúscula):
session = Session()

# Dados/registos de exemplo

# Departamentos
dep_estga = Departamento(nome="ESTGA")
dep_biologia = Departamento(nome="Biologia")

session.add_all([dep_estga, dep_biologia])
session.commit()

# Cursos
curso_rsi = Curso(nome="RSI", descricao="Redes e Sistemas Informáticos", departamento=dep_estga)
curso_bio = Curso(nome="Biologia", descricao="Licenciatura em Biologia", departamento=dep_biologia)

session.add_all([curso_rsi, curso_bio])
session.commit()

# Disciplinas
disc_prog = Disciplina(nome_uc="Programação Aplicada", ano=1, semestre=1, curso=curso_rsi)
disc_bd = Disciplina(nome_uc="Bases de Dados", ano=1, semestre=2, curso=curso_rsi)

session.add_all([disc_prog, disc_bd])
session.commit()


# Relação Possui (N‑N com atributos)
session.add(CursoDisciplina(curso=curso_rsi, disciplina=disc_prog, ano=1, semestre=1))
session.add(CursoDisciplina(curso=curso_rsi, disciplina=disc_bd, ano=1, semestre=2))
session.add(CursoDisciplina(curso=curso_bio, disciplina=disc_prog, ano=1, semestre=1))
session.commit()

# Alunos
aluno1 = Aluno(nmec=103477, nome="Inês Santos", data_nascimento=date(2002, 4, 10), morada="Aveiro")
aluno2 = Aluno(nmec=102222, nome="Rui Oliveira", data_nascimento=date(2000, 5, 17), morada="Águeda")

session.add_all([aluno1, aluno2])
session.commit()

# Inscrições
aluno1.disciplinas.append(disc_prog)
aluno1.disciplinas.append(disc_bd)
aluno2.disciplinas.append(disc_prog)



# Noutras situações reais, fazer bloco try...except no commit, porque os erros acontecem ao fazer commit
session.commit()        # commit final, neste caso

print("Base de dados criada.")

session.close()
engine.dispose()

