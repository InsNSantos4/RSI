BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Aluno" (
	"NMecanografico"	INTEGER NOT NULL UNIQUE,
	"Nome"	TEXT NOT NULL,
	"Data_Nascimento"	TEXT NOT NULL,
	"Morada"	TEXT NOT NULL,
	"id_curso"	INTEGER NOT NULL,
	PRIMARY KEY("NMecanografico"),
	FOREIGN KEY("id_curso") REFERENCES "Curso"("ID_curso")
);
CREATE TABLE IF NOT EXISTS "Curso" (
	"ID_curso"	INTEGER NOT NULL UNIQUE,
	"Nome_curso"	TEXT NOT NULL,
	"Descricao_curso"	TEXT NOT NULL,
	"id_departamento"	INTEGER NOT NULL,
	PRIMARY KEY("ID_curso"),
	FOREIGN KEY("id_departamento") REFERENCES "Departamento"("ID_dep")
);
CREATE TABLE IF NOT EXISTS "Departamento" (
	"ID_dep"	INTEGER NOT NULL UNIQUE,
	"Nome_dep"	TEXT NOT NULL,
	PRIMARY KEY("ID_dep")
);
CREATE TABLE IF NOT EXISTS "DisciplinaAluno" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"id_disciplina"	INTEGER NOT NULL,
	"NMec_aluno"	INTEGER NOT NULL,
	PRIMARY KEY("ID"),
	FOREIGN KEY("NMec_aluno") REFERENCES "Aluno"("NMecanografico"),
	FOREIGN KEY("id_disciplina") REFERENCES "Disciplinas"("ID_disciplina")
);
CREATE TABLE IF NOT EXISTS "DisciplinaCurso" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"id_curso"	INTEGER NOT NULL,
	"id_disciplina"	INTEGER NOT NULL,
	"Ano"	INTEGER NOT NULL,
	"Semestre"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("id_curso") REFERENCES "Curso"("ID_curso"),
	FOREIGN KEY("id_disciplina") REFERENCES "Disciplinas"("ID_disciplina")
);
CREATE TABLE IF NOT EXISTS "Disciplinas" (
	"ID_disciplina"	INTEGER NOT NULL UNIQUE,
	"Nome_UC"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("ID_disciplina")
);
COMMIT;
