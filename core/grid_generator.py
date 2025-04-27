import numpy as np
from random import randrange

def RandomProblemGenerator(nx, ny, qtd):
    map = np.zeros((nx, ny), int)
    
    k = 0
    while k < qtd:
        i = randrange(0, nx)
        j = randrange(0, ny)
        if map[i][j] == 0:
            map[i][j] = 9
            k += 1
    return map