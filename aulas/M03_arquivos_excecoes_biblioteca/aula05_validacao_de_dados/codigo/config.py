from pathlib import Path

caminho = Path("config.json")
try:
    texto = caminho.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Arquivo", caminho, "não existe. Usando a configuração padrão.")
    texto = "{}"
print("Configuração:", texto)
