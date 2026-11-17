texto = "Ação, coração, pão"
dados = texto.encode("utf-8")
print(dados)
print(len(texto), "caracteres e", len(dados), "bytes")

with open("errado.txt", "w", encoding="latin-1") as arquivo:
    arquivo.write(texto)

with open("errado.txt", encoding="utf-8", errors="replace") as arquivo:
    print(arquivo.read())
