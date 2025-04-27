from LinkedList import LinkedList
from math import sqrt

# Rotina sucessores para Grade de Ocupação
class WeightSearch:
    def __init__(self, grid, nx, ny):
        self.grid = grid
        self.dim_x = nx
        self.dim_y = ny
    
    def successorsGrid(self, actual):
        f = []
        x = actual[0]
        y = actual[1]
        
        if y + 1 != self.dim_y:
            if self.grid[x][y + 1] == 0:
                line = []
                line.append(x)
                line.append(y + 1)
                cost = 1
                line.append(cost)
                f.append(line)
                
        if x + 1 != self.dim_x:
            if self.grid[x + 1][y] == 0:
                line = []
                line.append(x + 1)
                line.append(y)
                cost = 3
                line.append(cost)
                f.append(line)
        
        if x - 1 >= 0:
            if self.grid[x - 1][y] == 0:
                line = []
                line.append(x - 1)
                line.append(y)
                cost = 2
                line.append(cost)
                f.append(line)
        
        if y - 1 >= 0:
            if self.grid[x][y - 1] == 0:
                line = []
                line.append(x)
                line.append(y - 1)
                cost = 4
                line.append(cost)
                f.append(line)
                
        return f
    
    @staticmethod # Foi necessário colocar para sinalizar que esse código não precisa do "self"
    def h(p1, p2):
        if p1[0] < p2[0]:
            m1 = 3 # valor do custo da rotina sucessores para esta acao
        else:
            m1 = 2 # valor do custo da rotina sucessores para esta acao
        
        if p1[1] < p2[1]:
            m2 = 1 # valor do custo da rotina sucessores para esta acao
        else:
            m2 = 4 # valor do custo da rotina sucessores para esta acao
        
        # heurística SEM movimento em diagonal
        #h = abs(p1[0] - p2[0]) * m1 + abs(p1[1] - p2[1]) * m2
        # heurística COM movimento em diagonal
        h = sqrt(m1 * (p1[0] - p2[0]) * (p1[0] -p2[0]) + m2 * (p1[1] - p2[1]) * (p1[1] - p2[1]))
        
        return h
    
    def uniformCostSearch(self, start, end): # Uniform Cost Search -> Working
        l1 = LinkedList()
        l2 = LinkedList()
        visitado = []
        l1.insereUltimo(start, 0, 0, None)
        l2.insereUltimo(start, 0, 0, None)
        linha = []
        linha.append(start)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            actual = l1.deletaPrimeiro()
            
            if tuple(actual.estado) == tuple(end):
                path = []
                path = l2.exibeCaminho2(actual.estado, actual.v1)
                
                return path, actual.v2
        
            filhos = self.successorsGrid(actual.estado)
            
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = actual.v2 + novo[2]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                
                for j in range(len(visitado)):
                    if visitado[j][0] == valor:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, actual)
                    l2.insereUltimo(valor, v1, v2, actual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return [], actual.v2
    
    def greedySearch(self, inicio, fim): # Greedy Search -> Working
        l1 = LinkedList()
        l2 = LinkedList()
        visitado = []
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            actual = l1.deletaPrimeiro()
            
            if tuple(actual.estado) == tuple(fim):
                
                caminho = []
                caminho = l2.exibeCaminho2(actual.estado, actual.v1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, actual.v2
        
            filhos = self.successorsGrid(actual.estado)            
            for novo in filhos:
                valor = (novo[0], novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = actual.v2 + novo[2]  # custo do caminho
                v1 = self.h(valor, fim) # f2(n)
                # print("Painel de Controle")
                # print("Estado atual: ", atual.estado)
                # print("V1: ", v1)
                # print("V2: ", v2)
                # print("Valor: ", valor)
                # print("Visitado: ", visitado)
                # print("---------------------------")

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==valor:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                            l1.inserePos_X(valor, v1, v2, actual)
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, actual)
                    l2.insereUltimo(valor, v1, v2, actual)
                    if flag2:
                        visitado.append([valor, v2])
                        
        return [], 0
    
    def aStarSearch(self, start, end): # A* Search -> Working
        l1 = LinkedList()
        l2 = LinkedList()
        visitado = []
        
        l1.insereUltimo(start, 0, 0, None)
        l2.insereUltimo(start, 0, 0, None)
        
        linha = []
        linha.append(start)
        linha.append(0)
        
        visitado.append(linha)
        
        while l1.vazio() == False:
            actual = l1.deletaPrimeiro()
            # print(atual.estado, atual.v2)
            
            if tuple(actual.estado) == tuple(end):
                path = []
                path = l2.exibeCaminho2(actual.estado, actual.v1)
                return path, actual.v2
        
            filhos = self.successorsGrid(actual.estado)
            
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = actual.v2 + novo[2]  # custo do caminho
            
                v1 = v2 + self.h(valor, end) # f3(n)

                flag1 = True
                flag2 = True
                
                for j in range(len(visitado)):
                    if visitado[j][0][0] == valor[0] and visitado[j][0][1] == valor[1]:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, actual)
                    l2.insereUltimo(valor, v1, v2, actual)
                    
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                        
        return [], 0

    def aiaStarSearch(self, start, end, limit):  # AIA* Search -> Working
        while True:
            lim_exc = []
            l1 = LinkedList()
            l2 = LinkedList()
            visitado = []
            l1.insereUltimo(start, 0, 0, None)
            l2.insereUltimo(start, 0, 0, None)
            linha = []
            linha.append(start)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() == False:
                actual = l1.deletaPrimeiro()
                
                if tuple(actual.estado) == tuple(end):
                    path = []
                    path = l2.exibeCaminho2(actual.estado, actual.v1)
                    return path, actual.v2
            
                filhos = self.successorsGrid(actual.estado)
                
                for novo in filhos:
                    valor = []
                    valor.append(novo[0])
                    valor.append(novo[1])
                    
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = actual.v2 + novo[2]  # custo do caminho
                    v1 = v2 + self.h(valor, end) # f3(n)
                    if v1 <= limit:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0] == valor:
                                if visitado[j][1] <= v2:
                                    flag1 = False
                                else:
                                    visitado[j][1] = v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(valor, v1, v2, actual)
                            l2.insereUltimo(valor, v1, v2, actual)
                            if flag2:
                                linha = []
                                linha.append(valor)
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
                        
            limit = float(sum(lim_exc) / len(lim_exc))
            
        return [], 0