# Módulo 01 · Desafio — Calculadora de terminal

> **Agora é com você.** Nada de código pronto: você vai construir sozinho um programa usando só o que viu nas Aulas 01 a 07.
> **Arquivos da entrega:** `calculadora.py` e `README.md`, na pasta `desafio_m01` do **seu repositório** no GitHub ([como entregar](../../../modelo-aluno/COMO-ENTREGAR.md)).

## 1. O que construir

Uma calculadora que roda no terminal, mostra um menu, faz a conta escolhida e **volta para o menu**, até a pessoa escolher sair.

Exemplo de como ela deve funcionar (o que está depois de `Opção:` e dos números foi digitado pelo usuário):

```
=== CALCULADORA PY ===

1-Somar 2-Subtrair 3-Multiplicar 4-Dividir 5-Potência 6-Resto 0-Sair
Opção: 1
Primeiro número: 8
Segundo número: 2
8.00 + 2.00 = 10.00

1-Somar 2-Subtrair 3-Multiplicar 4-Dividir 5-Potência 6-Resto 0-Sair
Opção: 9
Opção inválida. Escolha de 0 a 6.

1-Somar 2-Subtrair 3-Multiplicar 4-Dividir 5-Potência 6-Resto 0-Sair
Opção: 4
Primeiro número: 7
Segundo número: 0
Não dá para dividir por zero!

1-Somar 2-Subtrair 3-Multiplicar 4-Dividir 5-Potência 6-Resto 0-Sair
Opção: 0
Contas feitas: 1. Até a próxima!
```

O visual pode ser do seu jeito. O **comportamento** tem que ser este.

## 2. Requisitos obrigatórios

| # | Requisito | Aula que ajuda |
|---|---|---|
| R1 | Menu com 6 operações: somar, subtrair, multiplicar, dividir, potência e resto | 03 |
| R2 | O menu volta depois de cada conta; só termina com a opção `0` | 06 |
| R3 | Opção que não existe → aviso, e volta ao menu **sem pedir números** | 05 e 06 |
| R4 | Divisão ou resto por zero → aviso, sem o programa quebrar | 05 |
| R5 | Números com casas decimais (`8.5` funciona) e resultado com **duas casas** | 02 e 04 |
| R6 | Ao sair, mostra quantas contas foram feitas | 02 e 06 |
| R7 | `README.md` com: como rodar, o que o programa faz, uma limitação e **um bug que você encontrou** e como achou | 07 |

## 3. Regras do jogo

- Use **só o que vimos no módulo**: variáveis, `input`, `print`, f-strings, operadores, `if/elif/else`, `while`, `for`, `break` e `continue`.
- Não use funções (`def`), listas nem `try`: isso vem nos próximos módulos.
- Se a pessoa digitar texto no lugar de um número, o programa vai quebrar com `ValueError`. **Por enquanto, tudo bem**: escreva isso no README como limitação. Você resolve no Módulo 03.
- Pode pedir ajuda para entender um erro. Não pode copiar a solução pronta de ninguém (nem de IA): o objetivo é **você** treinar.

## 4. Por onde começar

1. Faça o menu aparecer e ler a opção. Rode.
2. Coloque o menu dentro de um `while True:` e saia com `break` quando a opção for `"0"`. Rode.
3. Faça **uma** operação (somar) funcionar do começo ao fim. Rode.
4. Acrescente as outras com `elif`, uma de cada vez, rodando a cada uma.
5. Trate a opção inválida e a divisão por zero. Dica: `continue` volta para o começo do laço.
6. Crie a variável que conta as contas e mostre no final.
7. Escreva o README.

> **Lembre:** `input()` sempre devolve texto. Compare a opção com `"1"` (texto), não com `1`.
> **Travou?** Leia o traceback de baixo para cima, ou coloque um `breakpoint()` e use `p opcao` para ver o que está chegando.

## 5. Teste antes de entregar

Rode e confira cada linha:

- [ ] `8` + `2` dá `10.00`
- [ ] `2` potência `10` dá `1024.00`
- [ ] `7` resto `3` dá `1.00`
- [ ] `7.5` dividido por `2` dá `3.75`
- [ ] opção `9` mostra o aviso e **não** pede números
- [ ] `7` dividido por `0` mostra o aviso e o menu volta
- [ ] a opção `0` encerra e mostra o total de contas

## 6. Desafios extras (opcionais)

- **Memória:** se a pessoa digitar `m` no lugar do primeiro número, use o resultado da última conta.
- **Três strikes:** depois de 3 opções inválidas **seguidas**, o programa encerra com uma mensagem.
- **Tabuada:** uma opção 7 que pede um número e mostra a tabuada dele com `for`.
- **Média da turma:** uma opção 8 que pergunta quantas notas são, lê todas com `for` e mostra a média.

## 7. Como vai ser avaliado

| Critério | Peso |
|---|---|
| Os requisitos R1 a R6 funcionam (testes da seção 5) | 6 |
| Código legível: nomes claros, indentação certa, sem repetição à toa | 2 |
| README completo, com o bug encontrado (R7) | 2 |
| Desafios extras | até +1 |

Ao terminar, você terá cumprido os critérios do módulo: **executa scripts sozinho**, **resolve problemas com decisões e laços** e **depura erros básicos**.
