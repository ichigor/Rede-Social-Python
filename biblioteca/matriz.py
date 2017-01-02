def listarDadosPerfil(perfis,redeSocial,p1):
    print("\n\n\n")
    print("Dados pessoa pesquisa")
    print(perfis[p1])
    print("Vinculos da pessoa pesquisada")
    for i in range(len(perfis)):
        if redeSocial[p1][i] !=0:
            print(perfis[i][1:2])

def sugestaoAmizade(perfis, redeSocial, p1,p2):
    print("\n\n\n")
    tipo=redeSocial[p1][p2]
    if tipo != 0:
        print("Pessoas que talvez voce conheça")
        for i in range(len(perfis)):
            if redeSocial[p2][i] !=0:
                print(perfis[i][1:2])
    elif tipo ==0:
        print("As pessoas pesquisadas nao sao amigos")

def rmvMatriz(redeSocial, x):
    for i in range(len(redeSocial)):
        del(redeSocial[i][x])
    for j in range(len(redeSocial)):
        if j == x:
            redeSocial.pop(j)
    return redeSocial

def addMatriz(redeSocial):
    for i in range(len(redeSocial)):
        redeSocial[i].append(0)
    linha = []
    for i in range(len(redeSocial)+1):
        linha.append(0)
    redeSocial.append(linha)
    return redeSocial

def addAmizade(rede,a,b):
    if rede[a][b] !=0 :
        print("\n\n\n\n")
        print("Essas pessoas ja sao amigas")
    else:
        opcao=int(input("Qual o seu nivel de amizade /1- Conhecido/ 2- Amigo / 3 - Familiar"))
        rede[a][b]=opcao
        rede[b][a]=opcao
        print("\n\n")
        print("Amizade realizada com sucesso ! :D")
    return rede

def rmvAmizade(rede,a,b):
    if rede[a][b] ==0 :
        print("\n\n\n\n")
        print("Essas pessoas nao sao amigas")
    else:
        rede[a][b]=0
        rede[b][a]=0
        print("\n\n")
        print("Amizade desfeita :(")
    return rede

def criarMatriz(perfis):
    #cria matriz com zeros nas posiçoes
    rede = []
    for i in range(len(perfis)):
        linha = []
        for j in range(len(perfis)):
            linha.append(0)
        rede.append(linha)
    return rede

def criarAmizades(redeSocial):
    redeSocial[0][1]=3
    redeSocial[1][0]=3
    redeSocial[2][0]=1
    redeSocial[0][2]=1
    redeSocial[3][0]=2
    redeSocial[0][3]=2
    redeSocial[2][5]=1
    redeSocial[5][2]=1
    redeSocial[3][4]=2
    redeSocial[4][3]=2
    redeSocial[4][5]=3
    redeSocial[5][4]=3
    return redeSocial


def printMatriz(redeSocial):
    for i in redeSocial:
        print(i)

def apresentarVinculos(rede,p1,p2, perfis):
    tipo=rede[p1][p2]
    if tipo == 1:
        print("As pessoas pesquisadas sao conhecidas")
        print(perfis[p1][1:3])
        print(perfis[p2][1:3])
    elif tipo ==2:
        print("As pessoas pesquisadas sao amigas")
        print(perfis[p1][1:4])
        print(perfis[p2][1:4])
    elif tipo ==3:
        print("As pessoas pesquisadas sao familiares")
        print(perfis[p1][1:])
        print(perfis[p2][1:])
    elif tipo ==0:
        print("As pessoas pesquisadas nao sao amigos")
