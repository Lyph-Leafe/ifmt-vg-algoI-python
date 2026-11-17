# Módulo 02 · Desafio — Gerenciador de contatos

> **Agora é com você.** Construa sozinho uma agenda de contatos usando listas, dicionários, funções e módulos (Aulas 01 a 07 do Módulo 02).
> **Arquivos da entrega:** `contatos.py`, `main.py` e `README.md`, na pasta `desafio_m02` do **seu repositório** no GitHub ([como entregar](../../../modelo-aluno/COMO-ENTREGAR.md)).

## 1. O que construir

Uma agenda de terminal que guarda contatos **em memória** e permite **cadastrar, listar, buscar, editar e excluir**.
Cada contato é um dicionário, e a agenda é uma lista desses dicionários:

```python
agenda = [
    {"nome": "Ana", "telefone": "98888-2222", "email": ""},
    {"nome": "Bia", "telefone": "99999-1111", "email": "bia@email.com"},
]
```

Exemplo de uso (o que vem depois de `Opção:` e dos `:` foi digitado pelo usuário):

```
=== AGENDA PY ===
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: 1
Nome: Bia
Telefone: 99999-1111
E-mail (Enter pula): bia@email.com
Bia cadastrado(a)!
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: 1
Nome: bia
Telefone: 1
E-mail (Enter pula):
Já existe um contato chamado bia.
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: 3
Buscar por: bi
1. Bia | 99999-1111 | bia@email.com
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: 0
Até mais! 1 contato(s) na agenda (e eles somem ao fechar).
```

## 2. Requisitos obrigatórios

| # | Requisito | Aula que ajuda |
|---|---|---|
| R1 | Contato = dicionário (`nome`, `telefone`, `email`); agenda = lista | 01 |
| R2 | **Cadastrar**, sem aceitar nome vazio nem nome repetido (`Bia` e `bia` são o mesmo) | 01 e 04 |
| R3 | **Listar** numerado e em ordem alfabética | 02 e 03 |
| R4 | **Buscar** por parte do nome (`bi` acha `Bia` e `Fabiana`) | 02 e 03 |
| R5 | **Editar** telefone e/ou e-mail; Enter vazio mantém o valor antigo | 04 e 05 |
| R6 | **Excluir** pelo nome, avisando se o contato não existe | 03 e 04 |
| R7 | **Uma função para cada tarefa**, todas com docstring, em `contatos.py`. Nenhuma delas usa `input` | 04 e 07 |
| R8 | O menu fica em `main.py`, que faz `import contatos` e tem `main()` com `if __name__ == "__main__":` | 06 e 07 |
| R9 | `README.md`: como rodar, o que cada arquivo tem, o que o programa faz e uma limitação | 07 |

## 3. Regras do jogo

- Use só o que vimos até aqui (Módulos 01 e 02). Nada de arquivos, `try` ou classes: isso vem depois.
- Ao fechar o programa, os contatos somem. **É esperado**: anote no README como limitação.
- `contatos.py` só **calcula e devolve**; quem conversa com o usuário (`input`) é o `main.py`. É isso que deixa as funções reutilizáveis.
- Pode pedir ajuda para entender um erro. Não pode copiar a solução pronta de ninguém (nem de IA).

## 4. Por onde começar

1. Em `contatos.py`, escreva `cadastrar(agenda, nome, telefone, email="")` e teste no próprio arquivo, dentro de `if __name__ == "__main__":`.
2. Escreva `mostrar(lista)` para imprimir os contatos. Teste.
3. Crie `main.py` com o menu (igual à calculadora do Módulo 01) e chame as duas funções.
4. Acrescente `buscar`, `editar` e `excluir`, uma por vez, testando cada uma.
5. Escreva as docstrings e o README.

**Ferramentas que vão ajudar:**

| Preciso de… | Use |
|---|---|
| comparar sem ligar para maiúsculas | `nome.lower()` (a mesma ideia do `key=str.lower` da Aula 03) |
| ver se um texto contém outro | `"bi" in "bia"` → `True` |
| filtrar uma lista | `[c for c in agenda if ...]` (Aula 03) |
| excluir | crie uma lista nova **sem** o contato, com uma comprehension |
| ordenar dicionários pelo nome | uma função `pegar_nome(contato)` que devolve o nome, e `sorted(agenda, key=pegar_nome)` |
| numerar a listagem | `enumerate(..., start=1)` (Aula 03) |
| editar só o que veio | `**kwargs`: `editar(agenda, "Ana", telefone="1234")` (Aula 05) |

> **Lembre:** uma função que procura e não acha pode devolver `None` (como o `dict.get` da Aula 07).

## 5. Teste antes de entregar

- [ ] cadastrar `Bia` e depois `bia` → o segundo é recusado
- [ ] cadastrar com nome vazio → recusado
- [ ] cadastrar `Caio`, `Ana` e `Bia` e listar → aparece Ana, Bia, Caio, numerados
- [ ] buscar `a` → acha os três; buscar `CA` → acha Caio; buscar `zé` → "nenhum"
- [ ] editar o telefone da Ana, deixando o e-mail vazio → só o telefone muda
- [ ] excluir `bia` → some da lista; excluir `zé` → aviso
- [ ] `python contatos.py` roda os testes do módulo **sem** abrir o menu
- [ ] `print(contatos.cadastrar.__doc__)` mostra a docstring

## 6. Desafios extras (opcionais)

- **Mais campos:** aniversário ou Instagram, sem mudar o menu (dica: `**kwargs`).
- **Favoritos:** marcar contatos com estrela e listar só eles.
- **Busca em tudo:** procurar também no telefone e no e-mail.
- **Estatística:** quantos contatos têm e-mail e quantos não têm.

## 7. Como vai ser avaliado

| Critério | Peso |
|---|---|
| R1 a R6 funcionam (testes da seção 5) | 5 |
| Organização: uma função por tarefa, sem `input` em `contatos.py`, sem código repetido (R7, R8) | 3 |
| Docstrings e README (R7, R9) | 2 |
| Desafios extras | até +1 |

Com isso você cumpre os critérios do módulo: **escolhe coleções adequadas**, **evita duplicação com funções** e **organiza módulos sem efeitos colaterais**.
