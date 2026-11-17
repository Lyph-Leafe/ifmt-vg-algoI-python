# Módulo 02 · Aula 07 — Docstrings e organização de um projeto simples

> **Você vai aprender:** documentar funções e organizar um projeto pequeno.
> **Código da aula:** `agenda.py`, `README.md`.

## 1. Uma função para cada tarefa

Em vez de um arquivo enorme de cima a baixo, divida em funções pequenas, cada uma com **uma** responsabilidade: `adicionar`, `buscar`, `listar`. Fica mais fácil de entender, testar e mudar.

## 2. Docstrings

Uma string entre **três aspas** logo na primeira linha da função (ou do arquivo) é a **docstring**: a documentação.

```python
def buscar(agenda, nome):
    """Devolve o telefone do contato, ou None se não existir."""
    return agenda.get(nome)
```

- Diga **o que** a função faz e **o que devolve**.
- O editor mostra a docstring quando você passa o mouse sobre a função.
- No código: `buscar.__doc__`.

> Comentário (`#`) explica **como** um trecho funciona; docstring explica **o que** a função faz, para quem vai usar.

## 3. `dict.get`

`agenda.get(nome)` devolve o valor ou `None` se a chave não existir (sem dar erro, ao contrário de `agenda[nome]`).

## 4. A função main

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

O programa principal fica numa função `main`, chamada só quando o arquivo é executado direto (Aula 06).

## 5. README.md

Todo projeto merece um `README.md`: o que ele faz e como rodar. É o primeiro arquivo que alguém lê (no GitHub, ele aparece na página do projeto). É escrito em **Markdown**: `#` para títulos, linhas com 4 espaços para código.

## Estrutura do projeto

```
agenda/
├── agenda.py     ← funções + main
└── README.md     ← o que é e como rodar
```

## Projeto do módulo

**Gerenciador de contatos em memória** com menu no terminal: cadastrar, buscar, editar, excluir e listar. Use um `while` com `input` para o menu, uma função para cada opção, docstrings em todas e um `README.md`.

➡️ Enunciado completo, requisitos e lista de testes: [Desafio do módulo](../desafio/apostila.md).
