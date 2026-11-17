from pathlib import Path

pasta = Path("dados")
pasta.mkdir(exist_ok=True)
arquivo = pasta / "notas.txt"
arquivo.write_text("Ana;9,5\n", encoding="utf-8")

print("Caminho:", arquivo)
print("Nome:", arquivo.name, "| Extensão:", arquivo.suffix)
print("Completo:", arquivo.resolve())
for item in pasta.iterdir():
    print("Na pasta:", item.name)
