# Módulo 02 · Aula 03 — Comprehensions, enumerate, zip e sorted

> **Você vai aprender:** quatro ferramentas que deixam o código com coleções mais curto e mais claro.
> **Código da aula:** `descontos.py`, `podio.py`, `ordenar.py`.

## 1. List comprehension

Criar uma lista nova a partir de outra, numa linha:

```python
# com for + append
com_desconto = []
for p in precos:
    com_desconto.append(p * 0.5)

# com comprehension
com_desconto = [p * 0.5 for p in precos]

# com filtro
baratos = [p for p in precos if p < 20]
```

Leia assim: "`p * 0.5` **para cada** `p` em `precos` (**se** `p < 20`)".

## 2. enumerate: a posição junto

```python
for posicao, nome in enumerate(podio, start=1):
    print(posicao, "lugar:", nome)
```

Sem `start`, a contagem começa no 0.

## 3. zip: duas listas lado a lado

```python
for aluno, nota in zip(alunos, notas):
    print(aluno, nota)
```

O `zip` para na lista **mais curta**.

## 4. sorted: ordenar sem estragar a original

- `sorted(lista)` devolve uma **lista nova** ordenada (o `.sort()` muda a própria lista).
- `reverse=True`: do maior para o menor.
- `key=`: o critério. `key=str.lower` ignora maiúsculas; `key=pontos.get` ordena as chaves de um dicionário pelo valor.

> Sem `key`, as maiúsculas vêm antes: `["Caio", "ana", "bia"]`.

## Exercícios

1. De uma lista de idades, crie com comprehension a lista só dos maiores de idade.
2. Crie `[n ** 2 for n in range(1, 11)]` e explique o resultado.
3. Mostre uma lista de tarefas numerada a partir de 1 com `enumerate`.
4. Com `zip`, junte uma lista de produtos e outra de preços e mostre "produto: R$ preço".
5. Ordene um dicionário de jogadores pelo número de vitórias, do maior para o menor.
