def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def situacao(m):
    if m >= 7:
        return "Aprovado"
    return "Recuperação"


m = media(8, 6.5, 7)
print(round(m, 1), situacao(m))
