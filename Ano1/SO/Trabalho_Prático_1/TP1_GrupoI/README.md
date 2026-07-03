# Relatório Trabalho Prático 1, Unidade Curricular de Sistemas Operativos:

---

## Sistema de Gestão de Tarefas e Entregas || handin_mgr shell script em bash

### Grupo I Ricardo Pulido (131393), Inês Santos (103477), Constança Rocha (135084)

---
---

# Descrição do Trabalho, por partes:

* O principal objetivo do trabalho consiste no desenvolvimento de um programa em Shell (POSIX sh) chamado handin_mgr que suporta dois conjuntos de funcionalidades: A) Gestão de tarefas (to-do) persistente; B) Gestão e validação de entregas de trabalhos (hand-ins).
* Estas funcionalidades obedecem a regras e formatos específicos que vão ser expostos nas secções seguintes, e o programa funciona em ambiente Unix/Linux com ferramentas standard do sistema.

# Parte A - Gestão de tarefas

* As tarefas criadas são guardadas localmente em $HOME/.handin_mgr/todos.csv com o formato:

```csv id;status;prio;due;tags;created;done;title```

* Em que: id é um inteiro positivo incremental; status: OPEN ou DONE; prio: inteiro (1 a 5), onde 5 é mais urgente; due: AAAA-MM-DD ou vazio; tags: lista separada por virgulas (ex: so,tp1,handin); created: timestamp ISO; done: timestamp ISO ou vazio; title: texto livre (pode conter espaços)

## Comandos disponíveis a serem executados:

### Comando todo-add com a seguinte sintaxe: 

```sh
handin_mgr todo-add "titulo" [-p P] [-d AAAA-MM-DD] [-t tag1,tag2]
```

#### Funcionalidades:

* Cria uma nova tarefa com status OPEN.
* Se -p não for indicado, prio default e 3.
* Se -d não for indicado, due fica vazio.
* Se -t não for indicado, tags fica vazio.
* id deve ser 1 + maior id existente (ou 1 se o ficheiro não existir).
* O comando deve criar o ficheiro todos.csv se não existir

* Robusto aos seguintes erros: Falta do titulo, prioridade fora de 1 a 5, data com formato inválido.

#### Exemplo(s) de utilização do todo-add

* Criar tarefa:

```sh
handin_mgr todo-add "Rever enunciado TP1" -p 4 -d 2026-02-20 -t so,tp1
```

* Criar tarefas:

```sh
shell> handin_mgr todo-add "projectoX" -p 2 -d 2027-12-06 -t so,tp
Criada tarefa 1
shell> handin_mgr todo-add "Teste1" -p 4 -d 2026-10-08 -t pr,ip
Criada tarefa 2
```

### Comando todo-list com a seguinte sintaxe:

```sh
handin_mgr todo-list [-a] [-s due|prio|created] [-t tag] [-p minPrio]
```

#### Funcionalidades:

* Por omissão lista apenas tarefas OPEN.
* Com -a lista OPEN e DONE.
* Filtragem:  -t tag lista apenas tarefas que contenham essa tag; -p minPrio lista apenas tarefas com prio >= minPrio.
* Ordenação: -s due: ordenar por due crescente (tarefas sem due no fim); -s prio: ordenar por prio decrescente; -s created: ordenar por created crescente; saída em formato legivel, por linha

* Robusto aos seguintes erros: sort inválido (não seja due, prio ou created); prioridade mínima fora de 1 a 5.

#### Exemplos de utilização do todo-list:

* Listar todas as tarefas

```sh
shell> handin_mgr todo-list -a
ID   STAT   PRIO  DUE          TAGS                 TITLE
1    TODO   2     2027-12-06   so,tp                "projectoX"
2    TODO   4     2026-10-08   pr,ip                "Teste1"
```

* Listar tarefas abertas ordenadas por prazo, por UC e por mínimo de prioridade (respetivamente):

```sh
shell> handin_mgr todo-list -a -s due
ID   STAT   PRIO  DUE          TAGS                 TITLE
2    DONE   4     2026-10-08   pr,ip                "Teste1"
1    TODO   2     2027-12-06   so,tp                "projectoX"

shell> handin_mgr todo-list -a -t so 
ID   STAT   PRIO  DUE          TAGS                 TITLE
1    TODO   2     2027-12-06   so,tp                "projectoX"

shell> handin_mgr todo-list -a -p 3
ID   STAT   PRIO  DUE          TAGS                 TITLE
2    DONE   4     2026-10-08   pr,ip                "Teste1"
```

### Comando todo-done com a seguinte sintaxe:

```sh
handin_mgr todo-done <id>
```

#### Funcionalidades:

* Marca a tarefa com esse id como DONE.
* Preenche o campo done com timestamp atual.
* Se ja estiver DONE, deve manter DONE e informar o utilizado (sem alterar done).

* Robusto a id inexistente e id inválido.

#### Exemplo(s) de utilização do todo-done

* Marcar tarefa concluída:

```sh
handin_mgr todo-done 3
```

* Marcar tarefa com id 2 como DONE:

```sh
shell> handin_mgr todo-done 2
Tarefa 2 marcada como DONE
shell> handin_mgr todo-list -a
ID   STAT   PRIO  DUE          TAGS                 TITLE
1    TODO   2     2027-12-06   so,tp                "projectoX"
2    DONE   4     2026-10-08   pr,ip                "Teste1"
```

### Comando todo-search com a seguinte sintaxe:

```sh
handin_mgr todo-search <texto>
```

#### Funcionalidades:

* Procura case-insensitive no campo title.
* Lista as tarefas correspondentes no mesmo formato do todo-list.

* Robusto à falta do texto.

#### Exemplo(s) de utilização do todo-search 

```sh
shell> handin_mgr todo-search "projecto"
ID   STAT   PRIO  DUE          TAGS                 TITLE
shell> handin_mgr todo-search Teste
ID   STAT   PRIO  DUE          TAGS                 TITLE
2    DONE   4     2026-10-08   pr,ip                "Teste1"
```

---

# Parte B - Gestão de entregas (handin)

## Comandos disponíveis a serem executados:

### Comando handin-ingest com a seguinte sintaxe:

```sh
handin_mgr handin-ingest <inbox_dir> <repo_dir> [-m]
```

#### Funcionalidades:

* Varre inbox_dir a procura de: diretorias cujo nome respeite a convenção; ficheiros .zip, .tar, .tar.gz cujo nome base respeite a convenção.
* Para cada entrega válida o nome e copia para o repositório.
* Se -m estiver presente, move em vez de copiar.
* Se a entrega for comprimida e existirem ferramentas para extrair: deve extrair para o destino final; o conteúdo extraido e que será validado em handin-check

* Relatório: deve criar runs/ingest_<timestamp>.txt com linhas do tipo:

```txt
OK;origem;destino
FAIL;origem;motivo
```

* Duplicados: se existirem várias entregas do mesmo ALUNO+UC+TP#, devem ser mantidas; o relatório deve marcar as entregas antigas como SUPERSEDED quando existir uma mais recente.

* Robusto aos seguintes erros: inbox_dir inexistente ou sem permissões; repo_dir inexistente ou sem permissões.

#### Exemplo(s) de utilização do handin-ingest

* Inserir entregas:

```sh
shell> handin_mgr handin-ingest /home/pulido/Desktop/Inicio /home/pulido/Desktop/Fim
Relatório: /home/pulido/.handin_mgr/runs/ingest_1775421067.txt
Ingest concluído.
```

### Ferramentas opcionais usadas (tar/unzip/gzip) e como o script se comporta sem elas:

Quanto às ferramentas opcionais, no handin-ingest usámos: o unzip, o .zip, o .tar.gz, o .tgz e o .tar, e a função não funciona se dentro da pasta de origem da entrega não houver ficheiros que tenham alguma extensão deste tipos.

---

### Comando handin-check com a seguinte sintaxe:

```sh
handin_mgr handin-check <repo_dir> [-o relatorio.csv]
```

#### Funcionalidades:

* Percorre todas as entregas dentro de repo_dir.
* Para cada entrega: valida nome e estrutura; confirma README e src/ com pelo menos 1 ficheiro; deteta proibidos (pastas, binarios, >5MB); calcula métricas: num_src_files: numero de ficheiros regulares em src/, total_files: numero total de ficheiros regulares, total_lines: total de linhas somadas de todos os ficheiros de texto em src/
* Produz um relatório: se -o for indicado, escreve no ficheiro, senão escreve em stdout.
* Formato por entrega (uma linha):

```csv
UC;TP#;ALUNO;timestamp;STATUS;num_src_files;total_files;total_lines;problemas
```

* Onde, na linha: STATUS pode ser OK ou FAIL; resistente aos seguintes problemas: vazio ou lista separada por vírgulas (ex:
missing_readme,binary_found,too_large)

Integração com todo:

* Sempre que uma entrega tiver STATUS FAIL, o script deve criar automaticamente uma tarefa OPEN em todos.csv com:

title: "Corrigir entrega ALUNO UC TP# (motivo)"

tags: handin,UC,TP#

prio: 5 se o erro for missing_src ou binary_found, senão 4.

#### Exemplos de utilização do handin-check

* Validar e gerar relatório para o stdout:

```sh
shell> handin_mgr handin-check /home/pulido/Desktop/Fim
Criada tarefa 3
Criada tarefa 4
Criada tarefa 5
Criada tarefa 6
Criada tarefa 7
UC;TP;ALUNO;timestamp;STATUS;num_src_files;total_files;total_lines;problemas
C;TP1;joao;202403251200;FAIL;0;2;0;missing_readme,missing_src,missing_src,binary_found
L;TP2;pedro;202405051845;FAIL;0;2;0;missing_readme,missing_src,missing_src,binary_found
S;TP1;carlos;202401101015;FAIL;0;2;0;missing_readme,missing_src,missing_src,binary_found
R;TP2;maria;202402141530;FAIL;0;2;0;missing_readme,missing_src,missing_src,binary_found
M;TP3;ana;202312011200;FAIL;1;3;5;binary_found
```

* Validar e gerar relatório para um ficheiro .csv:

```sh
shell> handin_mgr handin-check /home/pulido/Desktop/Fim -o /home/pulido/Desktop/entregas.csv
Criada tarefa 8
Criada tarefa 9
Criada tarefa 10
Criada tarefa 11
Criada tarefa 12
Relatório escrito em /home/pulido/Desktop/entregas.csv
```

### Comando handin-summary com a seguinte sintaxe:

```sh
handin_mgr handin-summary <repo_dir> [-u UC] [-t TPNº]
```

#### Funcionalidades:

Gera um resumo agregado das entregas (filtrado por UC e/ou TP se indicado):

* total de entregas
* numero de OK e FAIL
* top 5 entregas com mais ficheiros (total_files)
*top 5 entregas com mais linhas (total_lines)
* lista de alunos com pelo menos uma entrega FAIL (únicos)

Formato:

* Texto legível com secções e contagens.

#### Exemplos de utilização do handin-summary

* Resumo geral:

```sh
shell> handin_mgr handin-summary /home/pulido/Desktop/Fim
=== RESUMO DE ENTREGAS ===

Total de entregas: 5
OK: 1
FAIL: 4

=== Top 5 por número de ficheiros ===
3 M TP3 ana 202312011200
2 S TP1 carlos 202401101015
2 R TP2 maria 202402141530
2 L TP2 pedro 202405051845
2 C TP1 joao 202403251200

=== Top 5 por número de linhas ===
5 M TP3 ana 202312011200
0 S TP1 carlos 202401101015
0 R TP2 maria 202402141530
0 L TP2 pedro 202405051845
0 C TP1 joao 202403251200

=== Alunos com pelo menos uma entrega FAIL ===
joao
carlos
pedro
maria
```

* Resumo usando a opção de UC -u:

```sh
shell> handin_mgr handin-summary /home/pulido/Desktop/Fim -u M 
=== RESUMO DE ENTREGAS ===

Total de entregas: 1
OK: 1
FAIL: 

=== Top 5 por número de ficheiros ===
3 M TP3 ana 202312011200

=== Top 5 por número de linhas ===
5 M TP3 ana 202312011200

=== Alunos com pelo menos uma entrega FAIL ===
shell> handin_mgr handin-summary /home/pulido/Desktop/Fim -u M -t TP3
=== RESUMO DE ENTREGAS ===

Total de entregas: 1
OK: 1
FAIL: 

=== Top 5 por número de ficheiros ===
3 M TP3 ana 202312011200

=== Top 5 por número de linhas ===
5 M TP3 ana 202312011200

=== Alunos com pelo menos uma entrega FAIL ===
```

---

# Limitações e suposições do grupo acerca do trabalho:

Comentar a Integração (criar tarefas a partir de falhas):

> * Se, no handin_check, falhar algum dos critérios falhar, chama a função todo_add com as descrições de tudo o que falhou (título, aluno, UC, TP, prioridade) e porquê.

Comentar a robustez e qualidade (locks, erros, portabilidade, nomes com espaços, ajuda):

> * Locks funcionais baseados em mkdir atómico.
> * Erros: não usámos a função die, no entanto, através da função err retornamos com código de erro e a execução da shell continua.
> * Portabilidade: basta correr o ficheiro bash no terminal, da seguinte maneira e qualquer máquina Unix/Linux consegue correr o programa:
* \>> bash handin_mgr
> * É possível usar espaços nos argumentos dos comandos. Nenhuma das funções criadas é sensível ao uso de espaços, durante a sua utilização no terminal.
> * Existe uma função help geral com a estrutura de todos os comandos, mas também exite uma função individual para cada uma.

---

## Requisitos de implementação cumpridos:

* Utilizámos quoting correto em todas as expansões de variáveis e paths.
* Evitámos, quando possível, ler ficheiros linha a linha sem necessidade quando um pipeline resolve.
* Lidámos com ficheiros inexistentes (ex: todos.csv), criando-os quando apropriado.