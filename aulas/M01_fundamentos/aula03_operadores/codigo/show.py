idade = 16
print(idade >= 18)
print(idade == 16)
print(idade != 16)
print("python" == "Python")

tem_ingresso = True
com_responsavel = True
pode_entrar = tem_ingresso and (idade >= 18 or com_responsavel)
print("Pode entrar no show?", pode_entrar)
print(not tem_ingresso)
