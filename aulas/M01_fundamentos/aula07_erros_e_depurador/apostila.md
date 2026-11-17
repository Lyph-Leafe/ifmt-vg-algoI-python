# Módulo 01 · Aula 07 — Erros de sintaxe, de execução e o depurador

> **Você vai aprender:** ler mensagens de erro e investigar o programa passo a passo.
> **Código da aula:** `sintaxe.py`, `media_turma.py`, `depurar.py`.

## 1. Dois tipos de erro

| Tipo | Quando acontece | Exemplo |
|---|---|---|
| **De sintaxe** (`SyntaxError`) | antes de rodar: o código está mal escrito | `print("Olá"` sem fechar o parêntese |
| **De execução** (exceção) | durante a execução, numa situação que o código não previu | dividir por zero: `ZeroDivisionError` |

No erro de sintaxe, **nenhuma linha roda**. No de execução, o programa roda até a linha do problema.

## 2. Lendo o traceback

```
Traceback (most recent call last):
  File "media_turma.py", line 6, in <module>
    media = total / quantidade
ZeroDivisionError: division by zero
```

Leia **de baixo para cima**:
1. **Última linha:** o tipo do erro e o motivo.
2. **Acima:** o arquivo, o número da linha e o código que falhou.

Erros comuns: `NameError` (nome não existe, geralmente erro de digitação), `TypeError` (tipos misturados), `ValueError` (valor inválido, ex.: `int("abc")`), `IndentationError`, `ZeroDivisionError`.

## 3. O depurador

Depurar é rodar o programa **com pausas**, para ver o valor das variáveis. O jeito mais simples: coloque `breakpoint()` onde quer parar. No terminal aparece o prompt `(Pdb)`:

| Comando | Faz |
|---|---|
| `p variavel` | mostra o valor (ex.: `p i, total`) |
| `n` | roda a próxima linha |
| `c` | continua até o próximo `breakpoint()` |
| `q` | sai |

No Cursor/VS Code também existe o **depurador visual**: clique à esquerda do número da linha (bolinha vermelha) e aperte **F5**. As variáveis aparecem no painel lateral.

## Resumo

- Sintaxe: o código está mal escrito; nada roda.
- Execução: uma situação inesperada; roda até a linha do problema.
- Traceback: leia de baixo para cima.
- `breakpoint()` + `p` e `c` para investigar.

## Exercícios

1. Provoque de propósito um `NameError`, um `TypeError` e um `ValueError`. Anote a última linha de cada um.
2. Em `media_turma.py`, o que acontece se você digitar "dez" como nota? Qual é o erro?
3. Coloque um `breakpoint()` dentro da tabuada da Aula 06 e use `p i` em três voltas.
4. Use o depurador visual (F5) em `depurar.py` e observe `total` mudando.
