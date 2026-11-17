# Módulo 01 · Aula 04 — Entrada e saída: print, input e f-strings

> **Você vai aprender:** mostrar informações, ler dados do usuário e montar mensagens com f-strings.
> **Código da aula:** `codigo/saida.py`, `codigo/cadastro.py`, `codigo/lanche.py`.

## 1. print: saída

- Vários valores separados por vírgula saem separados por **espaço**.
- `sep="-"` troca o separador.
- `end="..."` troca o fim da linha (o padrão é pular linha).

```python
print("Python", "é", "legal", sep="-")   # Python-é-legal
print("Carregando", end="...")           # não pula linha
print("pronto!")                          # Carregando...pronto!
```

## 2. input: entrada

`input("pergunta")` mostra a pergunta, espera a pessoa digitar e apertar Enter, e devolve **sempre um texto** (`str`). Para fazer contas, converta:

```python
idade = int(input("Sua idade: "))       # inteiro
preco = float(input("Preço: R$ "))      # decimal (digite com ponto: 6.5)
```

## 3. f-strings

Coloque um `f` antes das aspas e escreva variáveis (ou contas) entre `{ }`:

```python
print(f"Olá, {nome}! Ano que vem você terá {idade + 1} anos.")
```

Para números decimais, `:.2f` mostra **duas casas**:

```python
total = 19.5
print(f"R$ {total:.2f}")    # R$ 19.50
```

| Formato | Resultado com `3.14159` |
|---|---|
| `{x}` | `3.14159` |
| `{x:.2f}` | `3.14` |
| `{x:.0f}` | `3` |

## Resumo

- `print` mostra; `sep` e `end` mudam o separador e o fim.
- `input` sempre devolve texto: use `int()` ou `float()`.
- f-string: `f"...{variavel}..."`; `:.2f` dá duas casas decimais.

## Exercícios

1. Peça o nome e o time favorito e mostre: `"Ana torce para o ___"` com f-string.
2. Peça a largura e a altura de um retângulo e mostre a área com duas casas.
3. Peça o preço de um produto e mostre o preço com 15% de desconto, formatado em reais.
4. Use `end` para mostrar `1 2 3 4 5` numa linha só, com 5 prints.
