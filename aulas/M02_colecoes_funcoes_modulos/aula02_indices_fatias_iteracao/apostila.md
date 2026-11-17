# Módulo 02 · Aula 02 — Indexação, fatias, iteração e operações comuns

> **Você vai aprender:** acessar itens pela posição, cortar pedaços e percorrer coleções.
> **Código da aula:** `ranking.py`, `notas.py`, `percorrer.py`.

## 1. Índices

```python
ranking = ["Ana", "Bia", "Caio", "Duda", "Edu"]
#            0      1      2       3      4
#           -5     -4     -3      -2     -1
```

- `ranking[0]` é o primeiro; `ranking[-1]` é o **último** (conta do fim).
- Índice que não existe dá `IndexError`.

## 2. Fatias: `[início:fim:passo]`

| Fatia | Resultado | Ideia |
|---|---|---|
| `ranking[0:3]` | Ana, Bia, Caio | o **fim não entra** |
| `ranking[2:]` | Caio, Duda, Edu | do 2 até o final |
| `ranking[:2]` | Ana, Bia | do começo até o 2 |
| `ranking[::-1]` | invertida | passo -1 anda de trás para frente |

Funciona igual em **textos**: `"@gamer_123"[1:]` dá `"gamer_123"`.

## 3. Operações comuns

| Operação | Faz |
|---|---|
| `len(lista)` | quantidade de itens |
| `max()` / `min()` | maior / menor |
| `sum()` | soma |
| `lista.sort()` | ordena a própria lista |
| `item in lista` | `True` se o item está na lista |

## 4. Percorrendo

```python
for item in inventario:          # lista: cada item
    print(item)

for nome, nota in notas.items(): # dicionário: chave e valor
    print(nome, nota)
```

## Exercícios

1. Com a lista `meses` (12 nomes), mostre o primeiro trimestre (fatia) e o último mês (índice negativo).
2. Peça uma palavra e diga se ela é um palíndromo (`palavra == palavra[::-1]`).
3. Dada uma lista de temperaturas da semana, mostre a maior, a menor e a média.
4. Percorra um dicionário `{"Matemática": 7, "Português": 9, "História": 6}` e mostre só as matérias com nota abaixo de 7.
