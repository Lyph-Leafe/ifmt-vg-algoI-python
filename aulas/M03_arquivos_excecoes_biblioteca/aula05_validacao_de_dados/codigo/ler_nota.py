def ler_inteiro(mensagem, minimo, maximo):
    while True:
        texto = input(mensagem)
        try:
            numero = int(texto)
        except ValueError:
            print("Isso não é um número inteiro. Tente de novo.")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"Digite um valor entre {minimo} e {maximo}.")


nota = ler_inteiro("Nota de 0 a 10: ", 0, 10)
print("Nota registrada:", nota)
