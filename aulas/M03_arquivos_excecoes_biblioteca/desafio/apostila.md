# Módulo 03 · Desafio — Agenda que não esquece: cadastro em JSON com backup

> **Agora é com você.** Pegue o seu gerenciador de contatos do Desafio do Módulo 02 e faça ele **guardar tudo em arquivo**, sobreviver a arquivo estragado e não quebrar com entrada errada.
> **Arquivos da entrega:** `main.py`, `contatos.py`, `armazenamento.py`, `entrada.py` e `README.md`, na pasta `desafio_m03` do **seu repositório** no GitHub ([como entregar](../../../modelo-aluno/COMO-ENTREGAR.md)).

## 1. O que construir

O mesmo menu do Módulo 02 (cadastrar, listar, buscar, editar, excluir), mas agora:

- os contatos ficam em `dados/contatos.json` e **voltam** quando você abre o programa de novo;
- antes de gravar, o arquivo anterior vira `dados/contatos_backup.json`;
- se o `contatos.json` estragar, o programa **avisa e recupera do backup**;
- letra no menu, nome vazio ou e-mail sem `@` **não quebram** o programa: ele pergunta de novo.

Exemplo, rodando duas vezes seguidas:

```
=== AGENDA PY ===
Nenhum contato salvo ainda. Começando com a agenda vazia.
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: 1
Nome: Ana
Telefone: 98888-2222
E-mail (Enter pula): ana.email
E-mail inválido: falta o @.
E-mail (Enter pula): ana@email.com
Ana cadastrado(a)!
(salvo)
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: abc
Isso não é um número inteiro. Tente de novo.
Opção: 0
Até mais! 1 contato(s) guardado(s) em dados\contatos.json.
```

```
=== AGENDA PY ===
1 contato(s) carregado(s) de dados\contatos.json.
1-Cadastrar 2-Listar 3-Buscar 4-Editar 5-Excluir 0-Sair
Opção: 2
1. Ana | 98888-2222 | ana@email.com
```

E com o arquivo estragado:

```
=== AGENDA PY ===
Atenção: dados\contatos.json está estragado.
Recuperei 1 contato(s) do backup.
```

## 2. Requisitos obrigatórios

| # | Requisito | Aula que ajuda |
|---|---|---|
| R1 | Ao iniciar, carrega `dados/contatos.json`; se não existir, começa vazia com aviso (`FileNotFoundError`) | 01, 03 e 05 |
| R2 | Depois de **cada** alteração (cadastrar, editar, excluir), grava a agenda em JSON com `with`, `encoding="utf-8"` e `ensure_ascii=False` | 02, 03 e 07 |
| R3 | Antes de gravar, copia o `contatos.json` atual (se estiver bom) para `contatos_backup.json` | 01 e 07 |
| R4 | `contatos.json` estragado → avisa e recupera do backup; sem backup bom → começa vazia, com aviso | 04 e 05 |
| R5 | Menu lido com uma função que repete até vir um inteiro de 0 a 5 | 05 |
| R6 | Nome e telefone obrigatórios; e-mail vazio ou com `@` | 05 |
| R7 | Caminhos com `pathlib` e relativos (`Path("dados") / "contatos.json"`), sem `C:\...` | 07 |
| R8 | Código dividido: `contatos.py` (do M02, **sem mudar**), `armazenamento.py`, `entrada.py` e `main.py`, com docstrings | M02 |
| R9 | `README.md`: como rodar, o que cada arquivo tem, **uma tabela de como cada erro é tratado** e como testar a recuperação | M02 · 07 |

## 3. Regras do jogo

- Use o que vimos até o Módulo 03. Nada de banco de dados ou classes: isso vem depois.
- Trate **só os erros que você sabe resolver**, cada um com o seu `except`. Nada de `except:` sozinho, que esconde bugs (Aula 04).
- Pode pedir ajuda para entender um erro. Não pode copiar a solução pronta de ninguém (nem de IA).

## 4. Por onde começar

1. Copie o seu `desafio_m02` para `desafio_m03`. Rode e confira que tudo ainda funciona.
2. Crie `armazenamento.py` com `salvar(agenda)` e chame depois do cadastrar. Rode e abra o `contatos.json` para ver.
3. Faça `carregar()` e use no começo do `main()`. Feche, abra de novo: os contatos voltaram?
4. Trate o `FileNotFoundError` (apague a pasta `dados` e rode).
5. Faça o backup no `salvar` e a recuperação no `carregar`. Estrague o arquivo de propósito para testar.
6. Crie `entrada.py` com as leituras validadas e troque os `input` do `main.py`.
7. README.

**Ferramentas que vão ajudar:**

| Preciso de… | Use |
|---|---|
| saber se o JSON está estragado | `json.load` lança `json.JSONDecodeError`, que **é um tipo de `ValueError`**: `except ValueError:` pega |
| copiar um arquivo | `destino.write_text(origem.read_text(encoding="utf-8"), encoding="utf-8")` |
| criar a pasta se não existir | `Path("dados").mkdir(exist_ok=True)` |
| ver se o arquivo existe | `caminho.exists()` |
| repetir até a entrada ficar boa | `while True` + `try`/`except ValueError` + `return` (a `ler_nota` da Aula 05) |
| ignorar espaços nas pontas | `texto.strip()` |
| rodar algo só se não deu erro | o bloco `else` do `try` (Aula 04) |

## 5. Teste antes de entregar

- [ ] apague a pasta `dados` e rode → "agenda vazia", sem traceback
- [ ] cadastre Ana, saia, rode de novo → Ana continua lá
- [ ] cadastre Bia → existe `contatos_backup.json` só com a Ana
- [ ] escreva `quebrado` dentro do `contatos.json` e rode → aviso + Ana recuperada do backup
- [ ] estrague também o backup → aviso + agenda vazia, sem traceback
- [ ] digite `abc` e `9` no menu → pede de novo
- [ ] nome só com espaços → pede de novo; e-mail `ana.email` → pede de novo
- [ ] cadastre `José` e abra o JSON: o acento aparece certo (não `\u00e9`)
- [ ] copie a pasta `desafio_m03` para outro lugar (ou outro PC) e rode de dentro dela: funciona sem mudar nada

## 6. Desafios extras (opcionais)

- **Histórico de backups:** em vez de um só, guarde `dados/backups/contatos_2026-11-16_20-30-05.json` (use `datetime.now().strftime(...)`, Aula 06) e mantenha só os 5 mais recentes.
- **Exportar para CSV:** uma opção 6 que gera `dados/contatos.csv` para abrir no Excel (veja `csv.DictWriter`).
- **Estatísticas:** com `Counter`, os domínios de e-mail mais usados (`gmail.com`, `hotmail.com`…).
- **Restaurar:** uma opção 7 que troca o `contatos.json` pelo backup, pedindo confirmação.

## 7. Como vai ser avaliado

| Critério | Peso |
|---|---|
| Persistência e backup funcionando (R1 a R4) | 4 |
| Entradas validadas, sem nenhum traceback nos testes da seção 5 (R5, R6) | 3 |
| Organização e caminhos portáveis (R7, R8) | 1 |
| README com a tabela de erros (R9) | 2 |
| Desafios extras | até +1 |

Com isso você cumpre os critérios do módulo: **lê e grava dados com segurança básica**, **trata erros de modo explícito** e **usa `with` sabendo por que o arquivo é fechado**.
