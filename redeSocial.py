from biblioteca import matriz
from biblioteca import perfil

perfis=[]
redeSocial=[]

perfis = [[0,"Gabriel","gabriel.redeSocial@gmail.com","5599864230","16/05/1995","Ens. Médio Completo"],
[1,"Luiz","luiz.redeSocial@gmail.com","5599864235","16/08/1995","Ens. Médio Completo"],
[2,"Maria","maria.redeSocial@gmail.com","5599864236","16/04/1995","Ens. Superior"],
[3,"Pedro","pedro.redeSocial@gmail.com","5599864231","17/05/1985","Ens. Basico"],
[4,"Gabriela","gabriela.redeSocial@gmail.com","5599864234","22/05/1995","Ens. Superior"],
[5,"Mauricio","mauricio.redeSocial@gmail.com","5599864245","24/01/1990","Ens. Superior"]]
redeSocial = matriz.criarMatriz(perfis)
redeSocial = matriz.criarAmizades(redeSocial)

valido = True
while valido :
    print("\n\n")
    matriz.printMatriz(redeSocial)
    print("\n\n")
    print("1 - Criar Conta")
    print("2 - Remover Conta")
    print("3 - Criar Amizade")
    print("4 - Cancelar Amizade")
    print("5 - Buscar sugestao de amizade")
    print("6 - Listar dados a partir do Vinculo de amizade")
    print("7 - Verificar Circulos de amizade")
    print("8 - Listar dados de um Perfil")
    print("\n\n")
    opcao=int(input("Qual operação deseja realizar: "))
    print("\n\n")
    if opcao >= 9:
        valido = False
    elif opcao == 1 :
        perfis=perfil.addPerfil(perfis)
        redeSocial = matriz.addMatriz(redeSocial)
    elif opcao == 2 :
        perfil.printPerfis(perfis)
        p1=int(input("Digite o numero da pessoa que deseja cancelar a conta: "))
        perfis=perfil.rmvPerfil(perfis,p1)
        redeSocial = matriz.rmvMatriz(redeSocial, p1)
    elif opcao == 3 :
        perfil.printPerfis(perfis)
        p1=int(input("Digite o numero da primeira pessoa que deseja tornar amiga: "))
        p2=int(input("Digite o numero da segunda pessoa que deseja tornar amiga: "))
        redeSocial = matriz.addAmizade(redeSocial,p1,p2)
    elif opcao == 4 :
        perfil.printPerfis(perfis)
        p1=int(input("Digite o numero da primeira pessoa que deseja desfazer amizade: "))
        p2=int(input("Digite o numero da segunda pessoa que deseja desfazer amizade: "))
        redeSocial = matriz.rmvAmizade(redeSocial,p1,p2)
    elif opcao == 5 :
        perfil.printPerfis(perfis)
        p1=int(input("Digite o numero da pessoa que deseja receber aviso de possiveis amigos: "))
        p2=int(input("Digite o numero da pessoa que tera amigos pesquisados: "))
        matriz.sugestaoAmizade(perfis, redeSocial, p1,p2)
    elif opcao == 6 :
        perfil.printPerfis(perfis)
        p1=int(input("Digite o numero da primeira pessoa que deseja pesquisar: "))
        p2=int(input("Digite o numero da segunda pessoa que deseja pesquisar: "))
        print("\n\n\n\n")
        matriz.apresentarVinculos(redeSocial,p1,p2,perfis)
    #elif opcao == 7 :
        #implementar CIRCULOS DE AMIZADE
        #procurarCirculos(perfis, redeSocial)
    elif opcao == 8:
        perfil.printPerfis(perfis)
        p1=int(input("Digite o numero da pessoa que deseja pesquisar: "))
        matriz.listarDadosPerfil(perfis,redeSocial,p1)
