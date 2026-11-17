# Módulo 01 · Aula 01 — Instalação, Cursor, terminal e o primeiro programa

> **Você vai aprender:** instalar o Python, usar o editor (Cursor ou VS Code), abrir o terminal e rodar um script.
> **Código da aula:** `codigo/ola.py`.

## 1. O que é Python

Python é uma **linguagem de programação**: um jeito de escrever instruções que o computador entende. Ele é usado em sites e apps (Instagram, YouTube), automação, ciência de dados, inteligência artificial e jogos. É uma das linguagens mais usadas do mundo e uma das mais fáceis de ler.

## 2. Instalando

1. Acesse **python.org › Downloads** e baixe a versão mais recente para o seu sistema.
2. No Windows, na primeira tela do instalador, marque **"Add python.exe to PATH"**. Sem isso, o terminal não acha o Python.
3. Clique em **Install Now** e espere terminar.
4. Instale um editor de código: o **Cursor** (cursor.com) ou o **VS Code** (code.visualstudio.com). O Cursor é baseado no VS Code: as telas e os atalhos são quase iguais.

## 3. O terminal

O terminal é onde você conversa com o computador por texto. No Cursor, abra em **Terminal › New Terminal**.

| Comando | O que faz |
|---|---|
| `python --version` | mostra a versão do Python instalada (confirma a instalação) |
| `dir` (Windows) / `ls` (Linux/Mac) | lista os arquivos da pasta atual |
| `cd nome_da_pasta` | entra numa pasta (`cd ..` volta uma) |
| `python arquivo.py` | roda um programa |
| `python` | abre o modo interativo (saia com `exit()`) |

## 4. O primeiro programa

Crie uma pasta para o curso, abra no Cursor (**File › Open Folder**) e crie o arquivo `ola.py`:

```python
print("Olá, mundo!")
print("Meu primeiro programa em Python")
```

- `print()` mostra uma mensagem na tela.
- O texto vai **entre aspas**.
- Cada linha é uma instrução; o Python lê **de cima para baixo**.

Rode no terminal: `python ola.py`. Antes, **salve** o arquivo (Ctrl+S).

## 5. O primeiro erro

Se você escrever `prnt` em vez de `print`, o Python mostra um **NameError**: ele não conhece esse nome. Errar é normal. Leia a **última linha** da mensagem: ela diz o tipo do erro e o motivo, e a linha de cima diz onde foi.

## 6. Se o `python --version` não funcionar

- **"python não é reconhecido como comando"**: faltou marcar *Add python.exe to PATH*. Rode o instalador de novo, escolha **Modify** (ou desinstale e instale de novo) e marque a opção.
- Depois de instalar, **feche e abra o terminal** (e o editor) de novo.
- Abriu a **Microsoft Store** ao digitar `python`? É um atalho do Windows: instale pelo python.org e desative em *Configurações › Aplicativos › Aliases de execução do aplicativo*.

## Links úteis

| Para | Link |
|---|---|
| Baixar o Python | https://www.python.org/downloads/ |
| Tutorial oficial (em português) | https://docs.python.org/pt-br/3/tutorial/ |
| Documentação | https://docs.python.org/pt-br/3/ |
| Editor Cursor | https://cursor.com |
| Editor VS Code | https://code.visualstudio.com |

## Resumo

- Python instalado e no PATH: `python --version` responde.
- Programas Python são arquivos `.py`; rode com `python nome.py`.
- `print()` mostra mensagens na tela.
- Mensagem de erro: comece lendo pela última linha.

## Exercícios

1. Crie `sobre_mim.py` com três `print`: seu nome, sua série e algo de que você gosta.
2. No modo interativo (`python`), calcule `365 * 24` (quantas horas tem um ano?).
3. Apague as aspas de um texto em `ola.py`, rode e leia o erro. Depois conserte.
4. Use `dir` e `cd` para navegar até a pasta do curso pelo terminal.
