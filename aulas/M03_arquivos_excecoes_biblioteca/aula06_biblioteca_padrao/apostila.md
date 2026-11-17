# Módulo 03 · Aula 06 — Biblioteca padrão: datetime, collections, itertools e statistics

> **Você vai aprender:** usar módulos prontos do Python para datas, contagens, combinações e estatística.
> **Código da aula:** `datas.py`, `votacao.py`, `estatistica.py`.

## "Baterias incluídas"

O Python vem com centenas de módulos prontos, a **biblioteca padrão**. Antes de escrever algo do zero (ou de instalar um pacote), vale procurar em docs.python.org/3/library.

## 1. datetime: datas

```python
from datetime import date, timedelta

hoje = date.today()
hoje.strftime("%d/%m/%Y")          # "16/11/2026"
hoje + timedelta(days=7)           # daqui a uma semana
(date(2027, 1, 1) - hoje).days     # dias entre duas datas
```

| Código | Significa |
|---|---|
| `%d` | dia |
| `%m` | mês |
| `%Y` | ano com 4 dígitos |
| `%H:%M` | hora e minuto |

## 2. collections.Counter: contar

```python
from collections import Counter
contagem = Counter(votos)
contagem.most_common(1)    # [('pizza', 3)]
```

## 3. statistics

| Função | Faz |
|---|---|
| `statistics.mean(lista)` | média |
| `statistics.median(lista)` | mediana (o valor do meio, com a lista ordenada) |
| `statistics.mode(lista)` | moda (o que mais aparece) |

## 4. itertools.combinations

```python
from itertools import combinations
combinations(["Ana", "Bia", "Caio"], 2)   # todas as duplas possíveis
```

## Outros módulos úteis

`random` (sorteios), `math` (raiz, pi, trigonometria), `os` e `pathlib` (pastas e arquivos), `time` (pausas e tempo), `json` e `csv` (Aula 03).

## Exercícios

1. Peça a data de nascimento (dia, mês, ano) e calcule quantos dias a pessoa já viveu.
2. Conte as letras de uma frase com `Counter` e mostre as 3 mais comuns.
3. Calcule média, mediana e moda das suas notas do bimestre.
4. Liste todos os confrontos possíveis entre 4 times com `combinations`.
