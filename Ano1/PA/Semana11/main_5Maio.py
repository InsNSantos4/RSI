from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Date, Table
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

Base = declarative_base()

# ============================================================
#  TABELA: Departamento (1) — (N) Curso
# ============================================================
class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)

    cursos = relationship("Curso", back_populates="departamento")

    def __str__(self):
        return f"Departamento(id={self.id}, nome={self.nome})"

    def __repr__(self):
        return self.__str__()


# ============================================================
#  TABELA ASSOCIATIVA: Curso — Disciplina (N‑N) com atributos
# ============================================================
class CursoDisciplina(Base):
    __tablename__ = "curso_disciplina"

    curso_id = Column(Integer, ForeignKey("curso.id"), primary_key=True)
    disciplina_id = Column(Integer, ForeignKey("disciplina.id"), primary_key=True)

    ano = Column(Integer, nullable=False)
    semestre = Column(Integer, nullable=False)

    curso = relationship("Curso", back_populates="disciplinas")
    disciplina = relationship("Disciplina", back_populates="cursos")

    def __str__(self):
        return f"CursoDisciplina(curso={self.curso_id}, disciplina={self.disciplina_id}, ano={self.ano}, semestre={self.semestre})"

    __repr__ = __str__


# ============================================================
#  TABELA: Curso
# ============================================================
class Curso(Base):
    __tablename__ = "curso"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    departamento_id = Column(Integer, ForeignKey("departamento.id"), nullable=False)
    departamento = relationship("Departamento", back_populates="cursos")

    # Relação N‑N com atributos
    disciplinas = relationship("CursoDisciplina", back_populates="curso")

    def __str__(self):
        return f"Curso(id={self.id}, nome={self.nome}, departamento={self.departamento.nome})"

    __repr__ = __str__


# ============================================================
#  TABELA ASSOCIATIVA: Aluno — Disciplina (N‑N)
# ============================================================
Inscrito = Table(
    "inscrito",
    Base.metadata,
    Column("aluno_id", Integer, ForeignKey("aluno.nmec"), primary_key=True),
    Column("disciplina_id", Integer, ForeignKey("disciplina.id"), primary_key=True)
)


# ============================================================
#  TABELA: Disciplina
# ============================================================
class Disciplina(Base):
    __tablename__ = "disciplina"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_uc = Column(String, nullable=False)

    # Relação N‑N com atributos
    cursos = relationship("CursoDisciplina", back_populates="disciplina")

    # Relação N‑N com alunos
    alunos = relationship("Aluno", secondary=Inscrito, back_populates="disciplinas")

    def __str__(self):
        return f"Disciplina(id={self.id}, nome_uc={self.nome_uc})"

    __repr__ = __str__


# ============================================================
#  TABELA: Aluno
# ============================================================
class Aluno(Base):
    __tablename__ = "aluno"

    nmec = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    morada = Column(String, nullable=False)

    disciplinas = relationship("Disciplina", secondary=Inscrito, back_populates="alunos")

    def __str__(self):
        return f"Aluno(nmec={self.nmec}, nome={self.nome})"

    __repr__ = __str__


# ============================================================
#  CRIAR BASE DE DADOS
# ============================================================
engine = create_engine("sqlite:///info_universidade.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# ============================================================
#  INSERIR DADOS DE EXEMPLO
# ============================================================

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

# Disciplinas (sem ano/semestre!)
disc_prog = Disciplina(nome_uc="Programação Aplicada")
disc_bd = Disciplina(nome_uc="Bases de Dados")

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

session.commit()

print("Base de dados criada com sucesso!")

session.close()
engine.dispose()
