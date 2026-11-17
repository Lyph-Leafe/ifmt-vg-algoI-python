precos = [10, 25, 40, 8]
com_desconto = []
for p in precos:
    com_desconto.append(p * 0.5)
print(com_desconto)

com_desconto = [p * 0.5 for p in precos]
print(com_desconto)

baratos = [p for p in precos if p < 20]
print(baratos)
