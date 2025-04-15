from LinkedList import listaDEnc

def gridSuccessors(state, grid, nx, ny):
    """Gera os sucessores válidos para um estado"""
    x, y = state
    moves = [
        (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),           # Cardinais
        (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)  # Diagonais
    ]
    
    validMoves = []
    for new_x, new_y in moves:
        if 0 <= new_x < nx and 0 <= new_y < ny and grid[new_x][new_y] == 0:
            validMoves.append([new_x, new_y])
    return validMoves

def amplitudeSearch(start_pos, end_pos, grid, nx, ny):
    """
    Realiza a busca em amplitude e retorna o caminho encontrado.
    Se não encontrar o caminho, retorna uma lista vazia.
    """
    l1 = listaDEnc()
    l2 = listaDEnc()
    
    l1.insereUltimo(start_pos, 0, 0, None)
    l2.insereUltimo(start_pos, 0, 0, None)
    
    visitado = [[start_pos, 0]]
    
    while not l1.vazio():
        atual = l1.deletaPrimeiro()
        
        for novo in gridSuccessors(atual.estado, grid, nx, ny):
            flag = True
            for aux in visitado:
                if aux[0] == novo:
                    if aux[1] <= (atual.v1 + 1):
                        flag = False
                    else:
                        aux[1] = atual.v1 + 1
                    break
            
            if flag:
                l1.insereUltimo(novo, atual.v1 + 1, 0, atual)
                l2.insereUltimo(novo, atual.v1 + 1, 0, atual)
                visitado.append([novo, atual.v1 + 1])
                
                if novo == list(end_pos):
                    return l2.exibeCaminho()
                    
    return []

