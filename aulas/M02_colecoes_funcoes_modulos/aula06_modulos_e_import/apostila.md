# Módulo 02 · Aula 06 — Módulos, pacotes, import e `if __name__ == "__main__"`

> **Você vai aprender:** dividir o programa em arquivos e reaproveitar código.
> **Código da aula:** `utilidades.py`, `main.py`.

## 1. Módulo = um arquivo .py

Todo arquivo `.py` é um **módulo**. Para usar as funções de `utilidades.py` em outro arquivo da mesma pasta:

```python
import utilidades
utilidades.area_retangulo(3, 4)
```

Ou trazendo só o que precisa:

```python
from random import randint
randint(1, 6)
```

## 2. Módulos prontos

O Python já vem com muitos módulos (a **biblioteca padrão**): `random` (sorteios), `math` (matemática), `datetime` (datas), `pathlib` (arquivos)... Veremos vários no Módulo 03.

## 3. O problema do código solto

Quando você importa um módulo, o Python **roda o arquivo inteiro**. Um `print` solto em `utilidades.py` aparece no `main.py`: é um efeito colateral.

## 4. `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    print("Testando:", area_retangulo(2, 5))
```

- `__name__` vale `"__main__"` quando o arquivo é **rodado direto** (`python utilidades.py`).
- Quando é **importado**, vale o nome do módulo (`"utilidades"`).

Então o que está dentro desse `if` só roda quando você executa o arquivo direto: ótimo para testes e para o "programa principal".

## 5. Pacotes

Um **pacote** é uma pasta com módulos (e, tradicionalmente, um arquivo `__init__.py`). Importa assim: `from jogo.personagens import criar`. Pacotes de terceiros se instalam com `pip install nome`.

## Exercícios

1. Crie `conversoes.py` com `km_para_milhas` e `celsius_para_fahrenheit`, e use num `main.py`.
2. Coloque um teste em `conversoes.py` dentro do `if __name__ == "__main__":` e confira que ele não aparece no `main.py`.
3. Use `from math import sqrt, pi` para calcular a área de um círculo e a raiz de 2.
4. Use `random.choice(lista)` para sortear quem apresenta o trabalho.
