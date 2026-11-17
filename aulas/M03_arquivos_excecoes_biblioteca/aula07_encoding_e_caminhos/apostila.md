# Módulo 03 · Aula 07 — Encoding, caminhos e portabilidade

> **Você vai aprender:** por que os acentos às vezes "quebram" e como escrever caminhos que funcionam em qualquer sistema.
> **Código da aula:** `acentos.py`, `caminhos.py`.

## 1. Texto vira bytes

O computador só guarda números (bytes). O **encoding** é a tabela que diz como cada caractere vira bytes. O padrão do mundo hoje é o **UTF-8**:

- letras sem acento: 1 byte;
- letras com acento (`ç`, `ã`): 2 bytes;
- emojis: 4 bytes.

`"Ação".encode("utf-8")` mostra os bytes: `b'A\xc3\xa7\xc3\xa3o'`.

## 2. Por que aparecem símbolos estranhos

Se um arquivo é **gravado** num encoding (ex.: `latin-1`, antigo no Windows) e **lido** em outro (`utf-8`), os bytes são interpretados errado: os acentos viram `�` ou `Ã§`.

**Regra:** sempre informe `encoding="utf-8"` ao abrir arquivos de texto, para ler e para escrever. Não dependa do padrão do sistema (que muda entre Windows, Linux e Mac).

## 3. Caminhos portáveis com pathlib

O Windows usa `\` (`dados\notas.txt`); Linux e Mac usam `/`. Com o `pathlib`, use `/` entre as partes e o Python acerta para cada sistema:

```python
from pathlib import Path

pasta = Path("dados")
pasta.mkdir(exist_ok=True)          # cria a pasta (sem erro se já existir)
arquivo = pasta / "notas.txt"       # junta as partes do caminho
arquivo.name      # "notas.txt"
arquivo.suffix    # ".txt"
arquivo.resolve() # caminho completo, desde a raiz do disco
for item in pasta.iterdir(): ...    # o que tem na pasta
```

## 4. Caminho relativo × absoluto

- **Relativo** (`dados/notas.txt`): a partir da pasta onde o programa está rodando. Funciona em qualquer computador. **Prefira.**
- **Absoluto** (`C:\Users\Ana\...`): só existe naquele computador.

## Projeto do módulo

**Sistema de cadastro persistido em JSON**, com backup e recuperação de erros de entrada: use o gerenciador de contatos do Módulo 02, salve em `dados/contatos.json` (com `pathlib` e `encoding="utf-8"`), carregue ao iniciar (tratando `FileNotFoundError`), valide as entradas (Aula 05) e, antes de salvar, copie o arquivo anterior para `contatos_backup.json`.

➡️ Enunciado completo, requisitos e lista de testes: [Desafio do módulo](../desafio/apostila.md).

## Exercícios

1. Quantos bytes tem a palavra "programação" em UTF-8? Calcule com `len(...encode("utf-8"))`.
2. Grave um texto com acentos em `latin-1` e leia em `latin-1`. Funciona? Por quê?
3. Crie a pasta `backup` e copie para lá um arquivo de texto usando `read_text` e `write_text`.
4. Liste todos os arquivos `.py` da pasta atual com `Path(".").glob("*.py")`.
