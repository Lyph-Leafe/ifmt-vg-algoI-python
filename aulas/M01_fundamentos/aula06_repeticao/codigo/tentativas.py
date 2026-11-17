tentativas = 0
senha = ""
while senha != "1234":
    senha = input("Senha: ")
    tentativas = tentativas + 1
print("Entrou depois de", tentativas, "tentativas")
