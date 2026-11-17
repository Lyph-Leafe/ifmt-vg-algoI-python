# Módulo 01 · Aula 05 — Condicionais: if, elif e else

> **Você vai aprender:** fazer o programa decidir o que fazer, dependendo de uma condição.
> **Código da aula:** `codigo/senha.py`, `codigo/nota.py`, `codigo/ingresso.py`.

## 1. if e else

```python
if senha == "python123":
    print("Acesso liberado!")
else:
    print("Senha incorreta.")
```

- Depois da condição vem **dois-pontos** `:`.
- As linhas de dentro ficam **recuadas** (4 espaços). É isso que diz ao Python o que está dentro do `if`.
- `else` é o caminho do contrário (opcional).

## 2. Indentação não é enfeite

Sem o recuo, o Python não sabe o que pertence ao `if` e mostra:

```
IndentationError: expected an indented block after 'if' statement on line 2
```

Use sempre **4 espaços** (o Cursor/VS Code faz isso com a tecla Tab).

## 3. elif: várias faixas

```python
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

O Python testa **de cima para baixo** e para na **primeira** condição verdadeira. Por isso a ordem importa: se `nota >= 5` viesse primeiro, quem tirou 9 cairia na recuperação.

## 4. Condições combinadas

```python
if idade < 12 or estudante == "s":
    print("Meia-entrada")
```

Use `and`, `or` e `not` (Aula 03) para juntar condições.

## Resumo

- `if condição:` + bloco recuado; `else:` para o contrário.
- `elif` cria faixas; vale a primeira condição verdadeira.
- Indentação de 4 espaços define o bloco; sem ela, `IndentationError`.

## Exercícios

1. Peça um número e diga se ele é par ou ímpar.
2. Peça a idade e classifique: criança (até 11), adolescente (12 a 17), adulto (18 ou mais).
3. Peça o valor de uma compra: acima de R$ 100, frete grátis; senão, frete de R$ 15. Mostre o total.
4. Peça usuário e senha; só libere se os dois estiverem certos (`and`).
