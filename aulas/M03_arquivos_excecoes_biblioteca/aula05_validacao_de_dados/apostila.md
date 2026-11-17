# Módulo 03 · Aula 05 — Exceções específicas e validação de dados

> **Você vai aprender:** garantir que o programa só aceite dados válidos.
> **Código da aula:** `ler_nota.py`, `config.py`.

## 1. Validar = conferir antes de usar

Dois tipos de problema:
- **tipo errado**: "dez" quando se espera um número → `ValueError` no `int()`;
- **valor fora da regra**: nota 15 quando a regra é de 0 a 10 → não é erro do Python, mas é erro de **regra**.

## 2. Pedir de novo até acertar

```python
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        texto = input(mensagem)
        try:
            numero = int(texto)
        except ValueError:
            print("Isso não é um número inteiro.")
            continue                     # volta para o começo do while
        if minimo <= numero <= maximo:
            return numero                # sai da função (e do while)
        print(f"Digite um valor entre {minimo} e {maximo}.")
```

- `while True` repete "para sempre"; quem sai é o `return`.
- `minimo <= numero <= maximo`: o Python aceita comparação encadeada.
- Uma função assim é **reutilizável**: idade, nota, quantidade, opção de menu...

## 3. Arquivo que não existe

```python
try:
    texto = caminho.read_text(encoding="utf-8")
except FileNotFoundError:
    texto = "{}"      # configuração padrão
```

Situação comum na primeira vez que um programa roda: ainda não existe arquivo salvo.

## 4. Boas práticas

- Trate a **exceção específica** (`ValueError`, `FileNotFoundError`), não "qualquer erro".
- Dê uma mensagem que diga **o que fazer** ("Digite um valor entre 0 e 10").
- Não esconda exceções que você não sabe resolver.

## Exercícios

1. Use `ler_inteiro` para pedir a idade (0 a 120) e a série (1 a 3).
2. Crie `ler_decimal(mensagem)` que aceita números com vírgula também (dica: `texto.replace(",", ".")`).
3. Crie `ler_opcao(mensagem, opcoes)` que só aceita uma opção da lista (ex.: `["s", "n"]`).
4. Junte com a Aula 03: carregue `contatos.json` se existir; se não, comece com um dicionário vazio.
