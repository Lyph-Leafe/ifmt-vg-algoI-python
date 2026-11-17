from datetime import date, timedelta

hoje = date.today()
print("Hoje:", hoje.strftime("%d/%m/%Y"))

prova = hoje + timedelta(days=7)
print("Prova em:", prova.strftime("%d/%m/%Y"))

ferias = date(hoje.year + 1, 1, 1)
print("Dias até o Ano Novo:", (ferias - hoje).days)
