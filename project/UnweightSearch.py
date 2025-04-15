from LinkedList import listaDEnc

class UnweightSearch:
    def __init__(self, grid, nx, ny):
        self.grid = grid
        self.nx = nx
        self.ny = ny

    def gridSuccessors(self, state):
        """Gera os sucessores válidos para um estado"""
        x, y = state
        moves = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),           # Movimentos cardinais
            (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)  # Movimentos diagonais
        ]
        validMoves = []
        for new_x, new_y in moves:
            if 0 <= new_x < self.nx and 0 <= new_y < self.ny and self.grid[new_x][new_y] == 0:
                validMoves.append([new_x, new_y])
        return validMoves

    def amplitudeSearch(self, start_pos, end_pos):
        """
        Busca em amplitude.
        Retorna o caminho encontrado ou uma lista vazia se não houver solução.
        """
        l1 = listaDEnc()
        l2 = listaDEnc()
        l1.insereUltimo(start_pos, 0, 0, None)
        l2.insereUltimo(start_pos, 0, 0, None)
        visitado = [[start_pos, 0]]
        
        while not l1.vazio():
            atual = l1.deletaPrimeiro()
            for novo in self.gridSuccessors(atual.estado):
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
    
    def depthSearch(self, start_pos, end_pos):
        """
        Busca em profundidade.
        Retorna o caminho encontrado ou uma lista vazia se não houver solução.
        """
        pilha = listaDEnc()
        visitados = set()
        pilha.insereUltimo(start_pos, 0, 0, None)
        visitados.add(tuple(start_pos))
        
        while not pilha.vazio():
            atual = pilha.deletaUltimo()
            if atual.estado == list(end_pos):
                caminho = []
                no = atual
                while no is not None:
                    caminho.insert(0, no.estado)
                    no = no.pai
                return caminho
            for vizinho in self.gridSuccessors(atual.estado):
                if tuple(vizinho) not in visitados:
                    visitados.add(tuple(vizinho))
                    pilha.insereUltimo(vizinho, 0, 0, atual)
        return []
    
    def verificaVisitado(self, novo, nivel, visitado):
        """
        Verifica se o nó 'novo' já foi visitado com um nível menor ou igual.
        Caso tenha sido visitado num nível maior, atualiza para o menor.
        """
        flag = True
        for aux in visitado:
            if aux[0] == novo:
                if aux[1] <= (nivel + 1):
                    flag = False
                else:
                    aux[1] = nivel + 1
                break
        return flag

    def depthLimitedSearch(self, start_pos, end_pos, limit):
        """
        Busca em profundidade limitada.
        Retorna o caminho encontrado ou None se o objetivo não for alcançado.
        """
        l1 = listaDEnc()  # Para busca
        l2 = listaDEnc()  # Para reconstruir o caminho
        l1.insereUltimo(start_pos, 0, 0, None)
        l2.insereUltimo(start_pos, 0, 0, None)
        visitado = [[start_pos, 0]]
        
        while not l1.vazio():
            atual = l1.deletaUltimo()
            if atual.v1 < limit:
                filhos = self.gridSuccessors(atual.estado)
                for novo in filhos:
                    if self.verificaVisitado(novo, atual.v1, visitado):
                        l1.insereUltimo(novo, atual.v1 + 1, 0, atual)
                        l2.insereUltimo(novo, atual.v1 + 1, 0, atual)
                        visitado.append([novo, atual.v1 + 1])
                        if novo == [end_pos[0], end_pos[1]]:
                            return l2.exibeCaminho()
        return None

    def iterativeDeepeningSearch(self, start_pos, end_pos):
        """
        Busca por aprofundamento iterativo.
        Aumenta gradativamente o limite até encontrar uma solução.
        Retorna o caminho encontrado ou uma lista vazia se não houver solução.
        """
        limite = 0
        while True:
            caminho = self.depthLimitedSearch(start_pos, end_pos, limite)
            if caminho:
                return caminho
            limite += 1
            if limite > self.nx * self.ny:  # Limite máximo (tamanho da grid)
                return []

    def bidirectionalSearch(self, start_pos, end_pos):
        """
        Busca bidirecional.
        Realiza a busca a partir do início e do fim simultaneamente.
        Retorna o caminho encontrado ou uma lista vazia se não houver solução.
        """
        l1 = listaDEnc()  # Busca a partir do início
        l2 = listaDEnc()  # Para reconstruir o caminho (início)
        l3 = listaDEnc()  # Busca a partir do fim
        l4 = listaDEnc()  # Para reconstruir o caminho (fim)
        l1.insereUltimo(start_pos, 0, 0, None)
        l2.insereUltimo(start_pos, 0, 0, None)
        l3.insereUltimo(end_pos, 0, 0, None)
        l4.insereUltimo(end_pos, 0, 0, None)
        visitado1 = [[start_pos, 0]]
        visitado2 = [[end_pos, 0]]
        ni = 0
        
        while not l1.vazio() or not l3.vazio():
            while not l1.vazio():
                if ni != l1.primeiro().v1:
                    break
                atual = l1.deletaPrimeiro()
                filhos = self.gridSuccessors(atual.estado)
                for novo in filhos:
                    if self.verificaVisitado(novo, atual.v1 + 1, visitado1):
                        l1.insereUltimo(novo, atual.v1 + 1, 0, atual)
                        l2.insereUltimo(novo, atual.v1 + 1, 0, atual)
                        visitado1.append([novo, atual.v1 + 1])
                        if not self.verificaVisitado(novo, atual.v1 + 1, visitado2):
                            caminho = [] + l2.exibeCaminho() + l4.exibeCaminho1(novo)
                            return caminho
            while not l3.vazio():
                if ni != l3.primeiro().v1:
                    break
                atual = l3.deletaPrimeiro()
                filhos = self.gridSuccessors(atual.estado)
                for novo in filhos:
                    if self.verificaVisitado(novo, atual.v1 + 1, visitado2):
                        l3.insereUltimo(novo, atual.v1 + 1, 0, atual)
                        l4.insereUltimo(novo, atual.v1 + 1, 0, atual)
                        visitado2.append([novo, atual.v1 + 1])
                        if not self.verificaVisitado(novo, atual.v1 + 1, visitado1):
                            caminho = [] + l4.exibeCaminho() + l2.exibeCaminho1(novo)
                            return caminho[::-1]
            ni += 1
        return []