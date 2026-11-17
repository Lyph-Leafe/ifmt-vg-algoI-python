# Módulo 01 · Aula 02 — Variáveis, tipos e conversão

> **Você vai aprender:** guardar informações em variáveis, reconhecer os tipos básicos do Python (`int`, `float`, `str`, `bool` e `None`) e converter um tipo em outro.
> **Código da aula:** pasta `codigo/` (`perfil.py`, `vidas.py`, `pontos.py`, `idade.py`).

## 1. Variável: um nome para um valor

Pense no perfil de um jogador num game: nome, nível, moedas, se está online. Cada informação dessas precisa ficar guardada em algum lugar. No programa, esse lugar é uma **variável**.

```python
nome = "Ana"
nivel = 12
```

O sinal `=` **não** é "igual" da matemática: ele quer dizer **guarde**. Lemos `nivel = 12` como "a variável `nivel` guarda 12". O valor fica do lado direito e o nome, do lado esquerdo.

**Regras para o nome:**
- letras, números e `_` (sublinhado); não pode começar com número;
- sem espaço e sem acento: `nivel`, e não `nível`;
- maiúscula e minúscula são diferentes: `Nome` e `nome` são variáveis diferentes;
- use nomes que explicam: `moedas` é melhor que `m`. Para várias palavras, use `_`: `pontos_por_fase`.

## 2. Os tipos básicos

Todo valor tem um **tipo**, e o tipo define o que dá para fazer com ele. A função `type()` mostra o tipo de qualquer valor.

| Tipo | O que é | Exemplo |
|---|---|---|
| `int` | número inteiro | `12`, `-3`, `0` |
| `float` | número com casas decimais (use **ponto**) | `1530.5`, `87.5` |
| `str` | texto, entre aspas simples ou duplas | `"Ana"`, `'oi'` |
| `bool` | verdadeiro ou falso | `True`, `False` |
| `NoneType` | "nada", ausência de valor | `None` |

Em `perfil.py`, o jogador ainda não entrou num clã, então `cla = None`. `None` é diferente de zero e de texto vazio: significa que **não tem valor**.

> **Atenção:** `True` e `False` começam com letra maiúscula. E `"12"` (com aspas) é texto, não número.

## 3. A variável pode mudar

O valor de uma variável pode ser trocado a qualquer momento (`vidas.py`):

```python
vidas = 3
vidas = vidas - 1   # pega o valor atual (3), tira 1 e guarda de novo: 2
```

No Python, a variável pode até mudar de tipo: `nivel = 12` e depois `nivel = "doze"`. Funciona, mas confunde quem lê o código. **Boa prática:** cada variável guarda sempre o mesmo tipo de informação.

## 4. Misturar tipos dá erro

```python
pontos = 100
print("Você fez " + pontos + " pontos")   # TypeError!
```

O `+` entre textos **junta** os textos; entre números, **soma**. Texto + número? O Python não adivinha e mostra:

```
TypeError: can only concatenate str (not "int") to str
```

Leia a **última linha** do erro: ela diz o tipo do erro (`TypeError`, erro de tipo) e o motivo. A solução é **converter** o número em texto com `str(pontos)`.

## 5. Conversão de tipos

| Função | Converte para | Exemplo | Resultado |
|---|---|---|---|
| `int()` | inteiro | `int("16")` | `16` |
| `float()` | decimal | `float("87.5")` | `87.5` |
| `str()` | texto | `str(100)` | `"100"` |
| `bool()` | verdadeiro/falso | `bool(0)` | `False` |

O caso mais comum é o `input()`: ele **sempre** devolve texto, mesmo que a pessoa digite um número. Por isso, para fazer conta com a idade (`idade.py`):

```python
idade = input("Quantos anos você tem? ")   # "16" (texto)
idade = int(idade)                          # 16 (número)
print("Ano que vem você vai ter", idade + 1, "anos")
```

E o `bool()`: zero e texto vazio viram `False`; qualquer outro número ou texto vira `True`.

> **Cuidado:** `int("dezesseis")` dá `ValueError`, porque o texto não é um número. Vamos aprender a tratar isso no Módulo 03.

## Resumo

- Variável = nome que guarda um valor; `=` quer dizer "guarde".
- Tipos básicos: `int`, `float`, `str`, `bool` e `None`. A função `type()` mostra o tipo.
- Texto + número dá `TypeError`: converta antes.
- `input()` sempre devolve `str`. Use `int()` ou `float()` para fazer contas.

## Exercícios

1. Crie `meu_perfil.py` com 5 variáveis sobre você (nome, idade, altura em metros, se gosta de games, sua série favorita) e mostre o tipo de cada uma.
2. Em `vidas.py`, acrescente uma linha que tire 2 vidas e mostre o resultado.
3. Faça um programa que pergunte o ano em que a pessoa nasceu e mostre quantos anos ela faz em 2030.
4. O que aparece em `print(int(7.9))`? E em `print(float(7))`? Rode e explique.
5. Desafio: por que `print("5" * 3)` mostra `555`? Teste e explique com suas palavras.
