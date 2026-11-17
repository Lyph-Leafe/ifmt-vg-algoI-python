idade = int(input("Idade: "))
estudante = input("É estudante? (s/n) ")
if idade < 12 or estudante == "s":
    print("Meia-entrada: R$ 15,00")
else:
    print("Inteira: R$ 30,00")
