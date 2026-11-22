# Estrutura base do trabalho

Este material serve apenas como ponto de partida para os alunos.

## Ideia da arquitetura

O programa deve arrancar diretamente em modo shell interativo.

- Ao executar `./handin_mgr`, o programa entra num ciclo `while`
- A shell permanece ativa ate o utilizador escrever `exit`
- Cada linha introduzida deve seguir o formato:

```sh
handin_mgr <comando> [opcoes] [args]
```

Exemplos:

```sh
handin_mgr todo-add "Rever enunciado" -p 4 -t so,tp1
handin_mgr todo-list -s due
handin_mgr handin-check /tmp/repo -o relatorio.csv
```

## O que o ficheiro base ja inclui

- organizacao geral do programa
- funcoes separadas por comando
- dispatcher central
- shell interativa com `while` e `exit`
- ajuda minima
- criacao da estrutura de estado persistente
- comentarios `TODO` nas partes a implementar

## O que falta aos alunos implementar

- parsing completo das opcoes
- validacoes de dados
- persistencia em CSV
- locks
- ingestao de entregas
- validacao de entregas
- relatorios e resumo agregado

## Nota importante

A shell fornecida no ficheiro base faz separacao simples por espacos:

```sh
set -- $cmdline
```

Por isso, nao trata aspas complexas como uma shell real. Isso foi deixado de forma simples de proposito, para os alunos poderem melhorar a implementacao.

## Sugestao de distribuicao

Distribuir aos alunos:

- `handin_mgr_base`
- este `README_base.md`

E explicar que podem reorganizar internamente a solucao, desde que mantenham a interface pedida no enunciado.
