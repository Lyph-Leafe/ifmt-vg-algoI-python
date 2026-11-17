# Módulo 03 · Aula 03 — CSV e JSON com a biblioteca padrão

> **Você vai aprender:** ler tabelas em CSV e salvar/carregar dados em JSON.
> **Código da aula:** `notas.csv`, `medias.py`, `perfil_json.py`.

## 1. CSV: uma tabela em texto

CSV (*comma-separated values*) é uma tabela: a primeira linha tem os nomes das colunas, e cada linha seguinte é um registro, com os valores separados por vírgula. Abre no Excel, no Google Planilhas e no Python.

```
nome,nota1,nota2
Ana,8.5,9.0
```

## 2. Lendo com `csv.DictReader`

```python
import csv

with open("notas.csv", encoding="utf-8", newline="") as arquivo:
    for linha in csv.DictReader(arquivo):
        print(linha["nome"], linha["nota1"])
```

- Cada linha vira um **dicionário**, com os nomes das colunas como chaves.
- Tudo vem como **texto**: converta com `float()` ou `int()` para fazer contas.
- `newline=""` é a recomendação oficial para arquivos CSV.

> Para escrever um CSV: `csv.DictWriter` (veja a documentação; é o exercício 3).

## 3. JSON: dados com estrutura

JSON é o formato que sites e apps usam para trocar dados. Ele parece um dicionário do Python, e aceita listas e dicionários dentro de dicionários.

```python
import json

with open("perfil.json", "w", encoding="utf-8") as arquivo:
    json.dump(perfil, arquivo, ensure_ascii=False, indent=2)   # salvar

with open("perfil.json", encoding="utf-8") as arquivo:
    carregado = json.load(arquivo)                             # carregar
```

- `indent=2` deixa o arquivo legível.
- `ensure_ascii=False` mantém os acentos como estão.

## CSV ou JSON?

| | CSV | JSON |
|---|---|---|
| Formato | tabela (linhas e colunas) | estrutura (listas, dicionários aninhados) |
| Bom para | planilhas, exportar para Excel | configurações, perfis, dados de apps |

## Exercícios

1. Acrescente um aluno no `notas.csv` e rode `medias.py` de novo.
2. Mostre só os alunos com média 7 ou mais.
3. Escreva um CSV com `csv.DictWriter` a partir de uma lista de dicionários.
4. Salve em JSON o placar de um jogo (`{"Ana": 1530, ...}`), carregue de volta e mostre o maior.
