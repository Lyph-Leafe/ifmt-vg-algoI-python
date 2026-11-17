# Módulo 02 · Aula 04 — Funções: definição, parâmetros, retorno e escopo

> **Você vai aprender:** criar funções, passar valores para elas e receber o resultado.
> **Código da aula:** `funcoes.py`, `boletim.py`, `escopo.py`.

## 1. Criando uma função

```python
def saudacao():
    print("Bem-vindo ao jogo!")

saudacao()   # chama a função
```

- `def` + nome + `()` + `:` e o bloco recuado.
- Definir **não roda** a função: ela só roda quando é **chamada**.
- Vantagem: escreve uma vez, usa quantas vezes quiser. Se precisar mudar, muda num lugar só.

## 2. Parâmetros e return

```python
def dobro(numero):     # numero é o parâmetro
    return numero * 2  # devolve o resultado

resultado = dobro(21)  # 42
```

| `print` | `return` |
|---|---|
| mostra na tela | **devolve** o valor para quem chamou |
| o valor se perde | dá para guardar numa variável e usar em contas |

O `return` também **encerra** a função na hora.

## 3. Funções usando funções

```python
m = media(8, 6.5, 7)       # 7.166...
print(round(m, 1), situacao(m))   # 7.2 Aprovado
```

`round(valor, 1)` arredonda para uma casa decimal.

## 4. Escopo

Variáveis criadas **dentro** de uma função são **locais**: só existem lá dentro. Em `escopo.py`, o `pontos = 10` de dentro da função é outra variável; o `pontos` de fora continua 0.

**Boa prática:** passe os valores por parâmetro e devolva com `return`, em vez de depender de variáveis de fora.

## Exercícios

1. Crie `area_circulo(raio)` que devolve `3.14159 * raio ** 2`.
2. Crie `eh_maior_de_idade(idade)` que devolve `True` ou `False`.
3. Crie `converter_temperatura(celsius)` que devolve em Fahrenheit (`c * 9 / 5 + 32`) e use num `for` de 0 a 40, de 10 em 10.
4. Refatore a tabuada da Aula 06 do M01 numa função `tabuada(numero)`.
