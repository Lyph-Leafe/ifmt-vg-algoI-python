from pathlib import Path

arquivo = Path("recados.txt")
arquivo.write_text("Prova de Python na sexta!\n", encoding="utf-8")
print("Arquivo existe?", arquivo.exists())
print(arquivo.read_text(encoding="utf-8"))
