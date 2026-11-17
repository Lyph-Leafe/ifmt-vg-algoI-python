with open("playlist.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Intro\n")
    arquivo.write("Hit do verão\n")
    arquivo.write("Acústico\n")

print("Fechado?", arquivo.closed)

with open("playlist.txt", encoding="utf-8") as arquivo:
    musicas = arquivo.read().splitlines()

print(musicas)
print("Total:", len(musicas))
