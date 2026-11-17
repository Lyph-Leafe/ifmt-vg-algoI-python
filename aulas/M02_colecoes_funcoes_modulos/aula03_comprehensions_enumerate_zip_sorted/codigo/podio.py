podio = ["Ana", "Caio", "Bia"]
for posicao, nome in enumerate(podio, start=1):
    print(posicao, "lugar:", nome)

alunos = ["Ana", "Bia", "Caio"]
notas = [8.5, 6.0, 9.5]
for aluno, nota in zip(alunos, notas):
    print(aluno, nota)
