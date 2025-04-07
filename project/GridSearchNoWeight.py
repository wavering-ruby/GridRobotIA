import numpy as np
from random import randrange

def Gera_Problema(nx, ny, qtd):
    mapa = np.zeros((nx, ny), int)
    
    k = 0
    while k < qtd:
        i = randrange(0, nx)
        j = randrange(0, ny)
        if mapa[i][j] == 0:
            mapa[i][j] = 9
            k += 1
    return mapa