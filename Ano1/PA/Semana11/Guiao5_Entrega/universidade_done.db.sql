BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Aluno" (
	"NMecanografico"	INTEGER NOT NULL,
	"Nome"	TEXT NOT NULL,
	"Data_Nascimento"	TEXT NOT NULL,
	"Morada"	TEXT NOT NULL,
	"id_curso"	INTEGER NOT NULL,
	PRIMARY KEY("NMecanografico","id_curso"),
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
	PRIMARY KEY("ID" AUTOINCREMENT),
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
INSERT INTO "Aluno" ("NMecanografico","Nome","Data_Nascimento","Morada","id_curso") VALUES (103477,'Inês Santos','2002-12-20','Rua Aveiro',2100);
INSERT INTO "Aluno" ("NMecanografico","Nome","Data_Nascimento","Morada","id_curso") VALUES (103477,'Inês Santos','2002-12-20','Rua Aveiro',8316);
INSERT INTO "Aluno" ("NMecanografico","Nome","Data_Nascimento","Morada","id_curso") VALUES (103477,'Inês Santos','2002-12-20','Rua Aveiro',8240);
INSERT INTO "Aluno" ("NMecanografico","Nome","Data_Nascimento","Morada","id_curso") VALUES (102536,'Constança Rocha','2005-3-31','Rua Vouga',2100);
INSERT INTO "Aluno" ("NMecanografico","Nome","Data_Nascimento","Morada","id_curso") VALUES (178162,'Ricardo Pulido','1997-8-15','Rua Pedralva',2100);
INSERT INTO "Aluno" ("NMecanografico","Nome","Data_Nascimento","Morada","id_curso") VALUES (156239,'Jéssica Fernandes','2002-11-21','Rua Águeda',8325);
INSERT INTO "Curso" ("ID_curso","Nome_curso","Descricao_curso","id_departamento") VALUES (2100,'RSI','Redes e Sistemas Informáticos',5);
INSERT INTO "Curso" ("ID_curso","Nome_curso","Descricao_curso","id_departamento") VALUES (8240,'MIECT','Mestrado Integrado em Engenharia de Computadores e Telemática',4);
INSERT INTO "Curso" ("ID_curso","Nome_curso","Descricao_curso","id_departamento") VALUES (8316,'LECI','Licenciatura em Engenharia de Computadores e Informática',4);
INSERT INTO "Curso" ("ID_curso","Nome_curso","Descricao_curso","id_departamento") VALUES (8325,'MTC','Licenciatura em Multimédia e Tecnologias da Comunicação',21);
INSERT INTO "Departamento" ("ID_dep","Nome_dep") VALUES (4,'deti');
INSERT INTO "Departamento" ("ID_dep","Nome_dep") VALUES (5,'estga');
INSERT INTO "Departamento" ("ID_dep","Nome_dep") VALUES (21,'deca');
INSERT INTO "DisciplinaCurso" ("ID","id_curso","id_disciplina","Ano","Semestre") VALUES (1,2100,18013,1,'Segundo');
INSERT INTO "DisciplinaCurso" ("ID","id_curso","id_disciplina","Ano","Semestre") VALUES (2,2100,18240,1,'Segundo');
INSERT INTO "DisciplinaCurso" ("ID","id_curso","id_disciplina","Ano","Semestre") VALUES (3,2100,18241,1,'Segundo');
INSERT INTO "DisciplinaCurso" ("ID","id_curso","id_disciplina","Ano","Semestre") VALUES (4,8325,40664,1,'Primeiro');
INSERT INTO "Disciplinas" ("ID_disciplina","Nome_UC") VALUES (18013,'Planeamento de Redes');
INSERT INTO "Disciplinas" ("ID_disciplina","Nome_UC") VALUES (18240,'Segurança em Redes e Sistemas Informáticos');
INSERT INTO "Disciplinas" ("ID_disciplina","Nome_UC") VALUES (18241,'Programação Aplicada');
INSERT INTO "Disciplinas" ("ID_disciplina","Nome_UC") VALUES (40664,'Teorias da Comunicação');
COMMIT;
