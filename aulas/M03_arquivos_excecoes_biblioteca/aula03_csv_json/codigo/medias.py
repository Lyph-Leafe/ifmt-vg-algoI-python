import csv

with open("notas.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        media = (float(linha["nota1"]) + float(linha["nota2"])) / 2
        print(linha["nome"], "- média", media)
