def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade


print(validar_idade(16))
print(validar_idade(-3))
