# Desafio M01 · Calculadora de terminal
# Enunciado: aulas/M01_fundamentos/desafio/apostila.md no material do curso
print("Digite as informacoes para fazer os calculos")
quantidade = 0
escolha = 1
while escolha != 0:
  print("Digite 1 par somar")
  print("Digite 2 par subtrair")
  print("Digite 3 para mutiplicar")
  print("Digite 4 para dividir")
  print("Digite 5 para potencia")
  print("Digite 6 para resto")
  print("Digite 0 para sair")
  escolha = int(input("Digite a sua escolha: "))
  
  while ( 7< escolha >= 0 ):
    print("escolha invalida")
    escolha = int(input("Digite a sua escolha: "))

  if escolha == 1:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = (numero1 + numero2)
    print(f"{numero1} + {numero2} = {resultado:.2f}")
    
  elif escolha == 2:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = (numero1 - numero2)
    print(f"{numero1} - {numero2} = {resultado:.2f}")
    quantidade +=1
    
  elif escolha == 3:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = (numero1 * numero2)
    print(f"{numero1} x {numero2} = {resultado:.2f}")
    quantidade +=1
    
  elif escolha == 4:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    while numero1 == 0 or numero2 == 0:
      print("Divisao invalida, impossivel dividir por zero!")
      continue
    resultado = (numero1 / numero2)
    print(f"{numero1} / {numero2} = {resultado:.2f}")
    quantidade +=1
    
  elif escolha == 5:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = (numero1 ** numero2)
    print(f"{numero1} ^ {numero2} = {resultado:.2f}")
    quantidade +=1
    
  elif escolha == 4:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    while numero1 == 0 or numero2 == 0:
      print("Resto invalida, impossivel fazer resto por zero!")
      continue
    resultado = (numero1 % numero2)
    print(f"{numero1} resto {numero2} = {resultado:.2f}")
    quantidade +=1

  elif escolha == 0:
    break

  print(f"Operações feitas: {quantidade}")


