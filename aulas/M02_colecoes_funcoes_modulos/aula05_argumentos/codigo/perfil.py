def perfil(nome, **dados):
    print("Perfil de", nome)
    for chave, valor in dados.items():
        print(" ", chave, "=", valor)


perfil("Ana", idade=16, cidade="Cuiabá", esporte="vôlei")
