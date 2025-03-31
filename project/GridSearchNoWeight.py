from GridSearch import buscaGridNP  
import numpy as np
from random import randrange

def Gera_Problema(nx,ny,qtd):
    mapa = np.zeros((nx, ny), int)
    
    k = 0
    while k<qtd:
        i = randrange(0,nx)
        j = randrange(0,ny)
        if mapa[i][j]==0:
            mapa[i][j] = 9
            k+=1
    return mapa


# PROGRAMA PRINCIPAL
nx  = 5
ny  = 5
qtd = 5
mapa = Gera_Problema(nx,ny,qtd)


# print("======== Mapa ========\n",mapa)
# print()

# sol = buscaGridNP()
# caminho = []

def Get_Origin():
    
    while True:
        print("Coordenada da origem: ")
        x  = int(input("X = "))
        y = int(input("Y =  "))
        if mapa[x][y]==0:
            break
        print("Coordenada inválida")

    origin = [x,y]
    return origin
def Get_Destiny():
    while True:
        print("Coordenada do destino: ")
        x  = int(input("X = "))
        y = int(input("Y =  "))
        if mapa[x][y]==0:
            break
        print("Coordenada inválida")

    destiny = [x,y]
    return destiny

# caminho = sol.amplitude(origem,destino,nx,ny,mapa)
# if caminho!=None:
#     print("\n*****AMPLITUDE*****")
#     print("Caminho: ",caminho)
#     print("Custo..: ",len(caminho)-1)
# else:
#     print("CAMINHO NÃO ENCONTRADO")
      
# caminho = sol.profundidade(origem,destino,nx,ny,mapa)
# if caminho!=None:
#     print("\n*****PROFUNDIDADE*****")
#     print("Caminho: ",caminho)
#     print("Custo..: ",len(caminho)-1)
# else:
#     print("CAMINHO NÃO ENCONTRADO")

"""      
    limite = 2
    caminho = sol.prof_limitada(origem, destino, limite)
    print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
    print("\nCusto: ",len(caminho)-1)
    
    limite = 3
    caminho = sol.prof_limitada(origem, destino, limite)
    print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
    print("\nCusto: ",len(caminho)-1)
    
    limite = 4
    caminho = sol.prof_limitada(origem, destino, limite)
    print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
    print("\nCusto: ",len(caminho)-1)
   
    limite_maximo = len(nos)
    caminho = sol.aprof_iterativo(origem, destino, limite_maximo)
    print("\n*****APROFUNDAMENTO ITERATIVO*****\n",caminho)
    print("\nCusto: ",len(caminho)-1)


    caminho = sol.bidirecional(origem,destino)
    print("\n*****BIDIRECIONAL*****\n",caminho)
"""