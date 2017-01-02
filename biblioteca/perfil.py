def rmvPerfil(perfis, x):
    for i in range(len(perfis)):
        if i == x:
            perfis.pop(i)
    return perfis

def printPerfis(perfis):
    for i in perfis:
        print(i[1:2])


def addPerfil(perfis):
    i = len(perfis)
    linha = []
    linha.append(i)
    linha.append(input("Digite seu nome: "))
    linha.append(input("Digite seu email: "))
    linha.append(input("Digite seu telefone: "))
    linha.append(input("Digite sua data de nascimento: "))
    linha.append(input("Digite sua formação: "))
    perfis.append(linha)
    return perfis
