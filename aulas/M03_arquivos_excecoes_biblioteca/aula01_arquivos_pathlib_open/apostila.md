# Módulo 03 · Aula 01 — Leitura e escrita de arquivos com pathlib e open

> **Você vai aprender:** salvar informações em arquivos e ler de volta.
> **Código da aula:** `recados.py`, `diario.py`.

## 1. Por que arquivos?

As variáveis ficam na **memória** e somem quando o programa termina. Para o programa "lembrar" (um placar, uma lista de tarefas, um cadastro), salve num **arquivo**, que fica no disco.

## 2. O jeito simples: pathlib

```python
from pathlib import Path

arquivo = Path("recados.txt")
arquivo.write_text("Prova na sexta!\n", encoding="utf-8")  # cria/substitui
texto = arquivo.read_text(encoding="utf-8")                # lê tudo
arquivo.exists()                                           # True/False
```

`\n` é a **quebra de linha** dentro de um texto.

## 3. open e os modos

```python
arquivo = open("diario.txt", "w", encoding="utf-8")
arquivo.write("Uma linha\n")
arquivo.close()
```

| Modo | Faz | Cuidado |
|---|---|---|
| `"w"` | escreve (cria o arquivo) | **apaga** o que tinha antes |
| `"a"` | acrescenta no fim | mantém o conteúdo |
| `"r"` | lê (é o padrão) | o arquivo precisa existir |

- Sempre feche com `close()`: só assim o conteúdo é gravado com segurança. Na próxima aula, o `with` faz isso sozinho.
- Para ler linha por linha: `for linha in arquivo:`. Use `linha.strip()` para tirar o `\n` do fim.
- Use sempre `encoding="utf-8"` para os acentos saírem certos (Aula 07).

## Exercícios

1. Crie `placar.txt` com o placar de um jogo e leia de volta.
2. Faça um programa que pergunte uma tarefa (input) e **acrescente** em `tarefas.txt` (modo `"a"`). Rode 3 vezes e veja o arquivo.
3. Leia `tarefas.txt` e mostre as tarefas numeradas.
4. O que acontece se você abrir com `"r"` um arquivo que não existe? Anote o nome do erro.
