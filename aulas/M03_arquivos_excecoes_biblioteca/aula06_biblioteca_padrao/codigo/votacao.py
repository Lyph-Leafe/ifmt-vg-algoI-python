from collections import Counter

votos = ["pizza", "hambúrguer", "pizza", "sushi", "pizza", "sushi"]
contagem = Counter(votos)
print(contagem)
print("Mais votado:", contagem.most_common(1))
