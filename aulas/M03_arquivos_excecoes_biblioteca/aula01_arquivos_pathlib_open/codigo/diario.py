arquivo = open("diario.txt", "w", encoding="utf-8")
arquivo.write("Hoje aprendi a criar arquivos.\n")
arquivo.close()

arquivo = open("diario.txt", "a", encoding="utf-8")
arquivo.write("E também a acrescentar linhas.\n")
arquivo.close()

arquivo = open("diario.txt", "r", encoding="utf-8")
for linha in arquivo:
    print(linha.strip())
arquivo.close()
