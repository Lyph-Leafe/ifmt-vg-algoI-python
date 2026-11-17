import statistics
from itertools import combinations

notas = [7.5, 9.0, 6.0, 8.5, 9.0]
print("Média:", statistics.mean(notas))
print("Mediana:", statistics.median(notas))
print("Moda:", statistics.mode(notas))

turma = ["Ana", "Bia", "Caio"]
for dupla in combinations(turma, 2):
    print(dupla)
