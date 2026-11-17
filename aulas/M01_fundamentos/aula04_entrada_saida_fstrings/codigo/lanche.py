lanche = input("Qual lanche? ")
preco = float(input("Preço: R$ "))
quantidade = int(input("Quantidade: "))
total = preco * quantidade
print(f"{quantidade}x {lanche} = R$ {total:.2f}")
