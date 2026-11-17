# Módulo 03 · Aula 02 — Context manager: o `with` para arquivos

> **Você vai aprender:** abrir arquivos com segurança, sem precisar lembrar do `close()`.
> **Código da aula:** `playlist_arquivo.py`.

## 1. O problema

```python
arquivo = open("playlist.txt", "w")
arquivo.write(...)   # e se der erro aqui?
arquivo.close()      # ...esta linha nunca roda
```

Se você esquecer o `close()` (ou se acontecer um erro antes dele), o arquivo pode ficar **aberto** e o conteúdo, incompleto.

## 2. O `with`

```python
with open("playlist.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Intro\n")
    arquivo.write("Hit do verão\n")
# aqui o arquivo já está fechado
```

- O arquivo fica aberto **só dentro do bloco recuado**.
- Ao sair do bloco (normalmente **ou por erro**), o Python fecha sozinho.
- `as arquivo` dá um nome para o arquivo aberto.

O `with` é um **gerenciador de contexto** (context manager): prepara algo no começo e garante a limpeza no fim. Ele também é usado com conexões de banco de dados, rede e outros recursos.

## 3. Lendo tudo de uma vez

```python
with open("playlist.txt", encoding="utf-8") as arquivo:
    musicas = arquivo.read().splitlines()
```

- `read()` lê o arquivo inteiro como um texto.
- `splitlines()` quebra o texto numa **lista de linhas** (já sem o `\n`).

## Regra de ouro

> Abriu arquivo? Use `with`.

## Exercícios

1. Reescreva o `diario.py` da Aula 01 usando `with` nas três partes.
2. Salve uma lista de 5 tarefas num arquivo, uma por linha, com `with` e um `for`.
3. Leia esse arquivo com `read().splitlines()` e mostre quantas tarefas são.
4. Explique com suas palavras por que o `with` é mais seguro que o `close()`.
