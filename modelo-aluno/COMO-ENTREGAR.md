# Como entregar os desafios

Você vai ter **um repositório seu** no GitHub com os três desafios. É como um portfólio: ao longo do curso, ele mostra o que você construiu.

```
algoI-python-seunome/
├── README.md          ← seu nome e o status de cada desafio
├── .gitignore
├── desafio_m01/       ← calculadora
├── desafio_m02/       ← gerenciador de contatos
└── desafio_m03/       ← cadastro em JSON
```

## Uma vez só: criar o repositório

1. Crie uma conta em [github.com](https://github.com) (use o e-mail que você mais usa).
2. Clique em **New repository** e dê o nome `algoI-python-seunome` (ex.: `algoI-python-anasilva`).
   Deixe **Public**, sem marcar nenhuma opção de README. Clique em **Create repository**.
3. Copie o conteúdo desta pasta `modelo-aluno` para uma pasta no seu computador com o mesmo nome do repositório.
4. No `README.md`, troque `Seu Nome` pelo seu nome e a turma.

## Enviar para o GitHub (terminal)

Abra o terminal **dentro da sua pasta** e rode, uma linha de cada vez:

```
git init -b main
git add .
git commit -m "Começando os desafios"
git remote add origin https://github.com/SEU-USUARIO/algoI-python-seunome.git
git push -u origin main
```

Na primeira vez, o Git pode pedir para você dizer quem é:

```
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

> **Sem Git no computador?** Na página do repositório, use **Add file › Upload files** e arraste as pastas. Funciona igual para a entrega.

## A cada desafio

1. Programe dentro da pasta do desafio (`desafio_m01`, ...), rodando sempre no terminal.
2. Salve o progresso no GitHub sempre que algo novo funcionar:

   ```
   git add .
   git commit -m "M01: soma e subtração funcionando"
   git push
   ```

   Commits pequenos e com mensagem clara contam a história do seu trabalho. O professor olha o histórico.
3. Quando terminar, marque o desafio como **entregue** no seu `README.md`, faça o último `push` e envie **o link do repositório** na tarefa do Moodle.

## Checklist da entrega

- [ ] o repositório é **público** e o link abre
- [ ] o programa roda com `python ...` de dentro da pasta do desafio
- [ ] o `README.md` do desafio está preenchido
- [ ] passei em todos os testes da seção "Teste antes de entregar" da apostila do desafio
