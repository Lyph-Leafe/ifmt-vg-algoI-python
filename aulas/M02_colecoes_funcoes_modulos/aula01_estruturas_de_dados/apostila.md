# Módulo 02 · Aula 01 — Listas, tuplas, conjuntos e dicionários

> **Você vai aprender:** guardar vários valores numa variável só, e escolher a coleção certa.
> **Código da aula:** `playlist.py`, `tupla.py`, `seguidores.py`, `ficha.py`.

## As quatro coleções

| Coleção | Escrita | Ordem? | Muda? | Repete? | Exemplo de uso |
|---|---|---|---|---|---|
| **list** (lista) | `[1, 2, 3]` | sim | sim | sim | playlist, fila, inventário |
| **tuple** (tupla) | `(10, 25)` | sim | **não** | sim | coordenada, cor RGB, data |
| **set** (conjunto) | `{"a", "b"}` | **não** | sim | **não** | seguidores, tags únicas |
| **dict** (dicionário) | `{"nome": "Ana"}` | sim | sim | chaves não | ficha, perfil, cadastro |

## Lista

```python
playlist = ["Intro", "Hit do verão", "Acústico"]
playlist.append("Remix")     # adiciona no fim
len(playlist)                # 4 itens
playlist[0]                  # "Intro" (a contagem começa no 0)
```

## Tupla

Como a lista, mas **não muda** depois de criada. Use para dados que andam juntos e não devem ser alterados: `posicao = (10, 25)`.

## Conjunto (set)

Sem ordem e **sem repetição**. Ótimo para comparar grupos:

```python
a & b    # interseção: o que está nos dois
a | b    # união: tudo, sem repetir
set(lista_com_repetidos)   # remove os repetidos
```

> A ordem em que um `set` aparece no `print` pode mudar a cada execução.

## Dicionário

Pares **chave: valor**. Você busca pelo nome da chave, não pela posição:

```python
aluno = {"nome": "Ana", "turma": "2B", "media": 8.5}
aluno["nome"]            # "Ana"
aluno["media"] = 9.0     # muda um valor
aluno["email"] = "..."   # cria uma chave nova
```

## Como escolher

- Uma sequência de coisas, que muda? **lista**.
- Valores fixos que andam juntos? **tupla**.
- Sem repetição, ou comparar grupos? **set**.
- Cada valor tem um nome (uma ficha)? **dicionário**.

## Exercícios

1. Crie uma lista com 5 jogos favoritos, adicione mais um e mostre quantos são.
2. Guarde a data do seu aniversário numa tupla (dia, mês) e mostre.
3. Duas turmas fizeram uma lista de matérias favoritas. Quais aparecem nas duas? Use `set` e `&`.
4. Crie um dicionário com o perfil de um personagem de jogo (nome, classe, nível, vida) e aumente o nível em 1.
