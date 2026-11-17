# Módulo 01 · Aula 03 — Operadores aritméticos, relacionais e lógicos

> **Você vai aprender:** fazer contas, comparar valores e combinar condições.
> **Código da aula:** `codigo/calculos.py`, `codigo/media.py`, `codigo/show.py`.

## 1. Aritméticos

| Operador | Operação | `17 ? 5` |
|---|---|---|
| `+` | soma | `22` |
| `-` | subtração | `12` |
| `*` | multiplicação | `85` |
| `/` | divisão (sempre dá `float`) | `3.4` |
| `//` | divisão inteira (descarta o resto) | `3` |
| `%` | resto da divisão | `2` |
| `**` | potência | `17 ** 2 = 289` |

O `%` é muito útil: `numero % 2 == 0` diz se um número é **par**.

## 2. Ordem das operações (precedência)

Igual na matemática: primeiro `**`, depois `*`, `/`, `//` e `%`, e por último `+` e `-`. Parênteses vêm antes de tudo.

```python
nota1 + nota2 / 2      # 7 + 4.5 = 11.5  (errado!)
(nota1 + nota2) / 2    # 16 / 2  = 8.0   (certo)
```

Na dúvida, **use parênteses**: deixam a conta mais clara para quem lê.

## 3. Relacionais (comparação)

O resultado de uma comparação é sempre um `bool`: `True` ou `False`.

| Operador | Pergunta |
|---|---|
| `==` | é igual? (dois sinais!) |
| `!=` | é diferente? |
| `>` / `<` | é maior? é menor? |
| `>=` / `<=` | é maior ou igual? menor ou igual? |

> `=` guarda um valor; `==` compara. E texto diferencia maiúsculas: `"python" == "Python"` é `False`.

## 4. Lógicos

| Operador | Resultado `True` quando… |
|---|---|
| `and` | as **duas** condições são verdadeiras |
| `or` | **pelo menos uma** é verdadeira |
| `not` | inverte: `not True` é `False` |

```python
pode_entrar = tem_ingresso and (idade >= 18 or com_responsavel)
```

Lê-se: tem ingresso **e** (é maior de idade **ou** está com responsável).

## Resumo

- `/` sempre dá `float`; `//` corta o resto; `%` dá o resto.
- Parênteses mandam na ordem das contas.
- Comparações dão `True` ou `False`; `==` compara, `=` guarda.
- `and` exige as duas; `or` basta uma; `not` inverte.

## Exercícios

1. Um ônibus leva 40 pessoas. Quantos ônibus completos para 175 alunos? Quantos sobram? (use `//` e `%`)
2. Calcule a média de 4 notas com parênteses e sem parênteses. Compare.
3. Escreva uma expressão que diga se um número é par **e** maior que 10.
4. Um app só libera o cadastro para quem tem 13 anos ou mais **ou** tem autorização dos pais. Escreva essa condição.
