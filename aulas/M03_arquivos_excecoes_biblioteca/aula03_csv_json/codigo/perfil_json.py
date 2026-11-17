import json

perfil = {"nome": "Ana", "nivel": 12, "conquistas": ["primeira vitória", "100 moedas"]}

with open("perfil.json", "w", encoding="utf-8") as arquivo:
    json.dump(perfil, arquivo, ensure_ascii=False, indent=2)

with open("perfil.json", encoding="utf-8") as arquivo:
    carregado = json.load(arquivo)

print(carregado["conquistas"])
