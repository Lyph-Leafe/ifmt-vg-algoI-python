"""Agenda de contatos simples (Módulo 02)."""


def adicionar(agenda, nome, telefone):
    """Adiciona um contato à agenda."""
    agenda[nome] = telefone


def buscar(agenda, nome):
    """Devolve o telefone do contato, ou None se não existir."""
    return agenda.get(nome)


def listar(agenda):
    """Mostra todos os contatos em ordem alfabética."""
    for nome in sorted(agenda):
        print(nome, "-", agenda[nome])


def main():
    agenda = {}
    adicionar(agenda, "Bia", "99999-1111")
    adicionar(agenda, "Ana", "98888-2222")
    listar(agenda)
    print("Telefone da Bia:", buscar(agenda, "Bia"))
    print("Telefone do Zé:", buscar(agenda, "Zé"))
    print(buscar.__doc__)


if __name__ == "__main__":
    main()
