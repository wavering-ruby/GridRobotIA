from math import sqrt
# Rotina sucessores para Grade de Ocupação
def sucessores(atual,mapa,dim_x,dim_y):
    f = []
    x = atual[0]
    y = atual[1]
    
    if y+1!=dim_y:
        if mapa[x][y+1]==1:
            linha = []
            linha.append(x)
            linha.append(y+1)
            custo = 1
            linha.append(custo)
            f.append(linha)
            
    if x+1!=dim_x:
        if mapa[x+1][y]==1:
            linha = []
            linha.append(x+1)
            linha.append(y)
            custo = 3
            linha.append(custo)
            f.append(linha)
            
    
    if x-1>=0:
        if mapa[x-1][y]==1:
            linha = []
            linha.append(x-1)
            linha.append(y)
            custo = 2
            linha.append(custo)
            f.append(linha)
            
    
    if y-1>=0:
        if mapa[x][y-1]==1:
            linha = []
            linha.append(x)
            linha.append(y-1)
            custo = 4
            linha.append(custo)
            f.append(linha)
            
    return f

def Gera_Ambiente(arquivo):
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        mapa.append(str1)
    
    return mapa, len(mapa), len(mapa[0])

def h(p1,p2):
    if p1[0]<p2[0]:
        m1 = 3 # valor do custo da rotina sucessores para esta acao
    else:
        m1 = 2 # valor do custo da rotina sucessores para esta acao
    
    if p1[1]<p2[1]:
        m2 = 1 # valor do custo da rotina sucessores para esta acao
    else:
        m2 = 4 # valor do custo da rotina sucessores para esta acao
    
    # heurística SEM movimento em diagonal
    h = abs(p1[0]-p2[0])*m1 + abs(p1[1]-p2[1])*m2
    # heurística COM movimento em diagonal
    #h = sqrt(m1*(p1[0]-p2[0])*(p1[0]-p2[0]) + m2*(p1[1]-p2[1])*(p1[1]-p2[1]))
    return h