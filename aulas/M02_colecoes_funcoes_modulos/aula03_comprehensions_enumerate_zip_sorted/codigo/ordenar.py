pontos = {"Ana": 1530, "Bia": 2100, "Caio": 980}
ranking = sorted(pontos, key=pontos.get, reverse=True)
print(ranking)

nomes = ["bia", "Caio", "ana"]
print(sorted(nomes))
print(sorted(nomes, key=str.lower))
