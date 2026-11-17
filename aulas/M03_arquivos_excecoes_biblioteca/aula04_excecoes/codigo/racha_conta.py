try:
    total = float(input("Valor da conta: "))
    pessoas = int(input("Dividir por quantas pessoas? "))
    parte = total / pessoas
except ValueError:
    print("Digite apenas números.")
except ZeroDivisionError:
    print("Não dá para dividir por zero pessoas!")
else:
    print(f"Cada um paga R$ {parte:.2f}")
finally:
    print("Obrigado por usar a calculadora.")
