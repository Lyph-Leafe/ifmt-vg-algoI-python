# Módulo 01 · Aula 06 — Repetição: for, while, range, break e continue

> **Você vai aprender:** repetir instruções sem copiar e colar código.
> **Código da aula:** `contagem.py`, `tabuada.py`, `tentativas.py`, `pulos.py`.

## 1. for + range

```python
for i in range(1, 6):
    print("Volta", i)
```

O `for` repete o bloco recuado **uma vez para cada valor**. A variável `i` recebe 1, 2, 3, 4 e 5.

| `range` | Gera |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 (o fim **não entra**) |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 (de 2 em 2) |

O `for` também percorre um texto, letra por letra: `for letra in "Python":`.

## 2. while: enquanto for verdade

```python
while senha != "1234":
    senha = input("Senha: ")
```

Repete **enquanto** a condição for verdadeira. Use quando você **não sabe** quantas vezes vai repetir (ex.: até o usuário acertar).

> **Cuidado com o laço infinito:** se nada dentro do `while` mudar a condição, ele nunca para. Para interromper no terminal: **Ctrl+C**.

## 3. break e continue

- `continue`: **pula** o resto desta volta e vai para a próxima.
- `break`: **sai** do laço na hora.

```python
for numero in range(1, 21):
    if numero % 2 == 0:
        continue          # pula os pares
    if numero > 11:
        break             # para depois do 11
    print(numero)         # 1 3 5 7 9 11
```

## Resumo

- `for` + `range`: quando você sabe quantas vezes repetir.
- `while`: repete enquanto a condição for verdadeira.
- `continue` pula a volta; `break` sai do laço.

## Exercícios

1. Mostre a contagem regressiva de 10 até 1 e depois "Feliz Ano Novo!" (dica: `range(10, 0, -1)`).
2. Some os números de 1 a 100 com `for`. O resultado é 5050?
3. Peça números até o usuário digitar 0 e mostre a soma de todos.
4. Jogo de adivinhação: sorteie um número de 1 a 10 (`import random`, `random.randint(1, 10)`) e dê no máximo 3 tentativas.
