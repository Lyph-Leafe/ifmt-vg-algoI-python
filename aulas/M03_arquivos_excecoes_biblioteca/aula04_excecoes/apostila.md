# Módulo 03 · Aula 04 — Tratamento de exceções: try, except, else, finally e raise

> **Você vai aprender:** impedir que um erro derrube o programa, e lançar os seus próprios erros.
> **Código da aula:** `racha_conta.py`, `validar_idade.py`.

## 1. Exceção

Uma **exceção** é um erro durante a execução (Aula 07 do M01): `ValueError`, `ZeroDivisionError`, `FileNotFoundError`... Sem tratamento, o programa para e mostra o traceback.

## 2. try / except

```python
try:
    pessoas = int(input("Quantas pessoas? "))
    parte = total / pessoas
except ValueError:
    print("Digite apenas números.")
except ZeroDivisionError:
    print("Não dá para dividir por zero!")
```

- O Python **tenta** o bloco do `try`.
- Se acontecer uma exceção, ele **pula** para o `except` daquele tipo.
- Trate **tipos específicos**: cada erro com a mensagem certa.

## 3. else e finally

| Bloco | Roda quando |
|---|---|
| `try` | sempre (até o erro, se houver) |
| `except Tipo` | deu aquele tipo de erro |
| `else` | **não** deu erro nenhum |
| `finally` | **sempre**, com ou sem erro (ótimo para "limpeza") |

## 4. raise: lançando o seu erro

```python
def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade
```

Use `raise` quando a sua função recebe um valor que não faz sentido. Quem chamou decide como tratar.

> **Não esconda erros:** `except: pass` (pegar tudo e não fazer nada) deixa os bugs invisíveis. Trate só o que você sabe resolver.

## Exercícios

1. Peça dois números e mostre a divisão, tratando `ValueError` e `ZeroDivisionError`.
2. Na média da turma (M01, Aula 07), trate o caso de 0 notas.
3. Crie `validar_nota(nota)` que lança `ValueError` se a nota estiver fora de 0 a 10. Chame dentro de um `try`.
4. Use `finally` para sempre mostrar "Fim do programa".
