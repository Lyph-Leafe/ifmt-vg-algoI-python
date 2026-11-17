# Módulo 02 · Aula 05 — Argumentos: posicionais, nomeados, padrão, *args e **kwargs

> **Você vai aprender:** deixar suas funções mais flexíveis.
> **Código da aula:** `personagem.py`, `somar.py`, `perfil.py`.

## 1. Posicionais e nomeados

```python
criar_personagem("Rex", "guerreiro", 5)                    # pela posição
criar_personagem(classe="arqueira", nome="Kira", nivel=3)  # pelo nome
```

Com o nome, a ordem não importa e o código fica mais legível.

## 2. Valor padrão

```python
def criar_personagem(nome, classe, nivel=1):
```

Se ninguém passar o `nivel`, ele vale 1. Parâmetros com padrão vêm **depois** dos obrigatórios.

## 3. *args: quantos valores quiser

```python
def somar(*numeros):
    return sum(numeros)

somar(2, 3)          # 5
somar(1, 2, 3, 4, 5) # 15
```

Lá dentro, `numeros` é uma **tupla** com tudo o que foi passado.

## 4. **kwargs: pares nome=valor

```python
def perfil(nome, **dados):
    for chave, valor in dados.items():
        print(chave, valor)

perfil("Ana", idade=16, cidade="Cuiabá")
```

Lá dentro, `dados` é um **dicionário**.

> Os nomes `args` e `kwargs` são só convenção: o que importa é o `*` e o `**`.

## Ordem dos parâmetros

`def f(obrigatorios, com_padrao=..., *args, **kwargs)`

## Exercícios

1. Crie `saudacao(nome, mensagem="Olá")` e chame com e sem a mensagem.
2. Crie `maior(*numeros)` que devolve o maior valor recebido.
3. Crie `pedido(cliente, **itens)` que mostra cada item e a quantidade: `pedido("Bia", pizza=2, suco=3)`.
4. Chame uma função sua usando só argumentos nomeados, em ordem trocada.
