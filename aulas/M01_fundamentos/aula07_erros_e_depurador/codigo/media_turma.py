total = 0
quantidade = int(input("Quantas notas? "))
for i in range(quantidade):
    nota = float(input("Nota: "))
    total = total + nota
media = total / quantidade
print("Média:", media)
