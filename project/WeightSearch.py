import random as rd
import Node
from LinkedList import listaDEnc
from math import sqrt

# Rotina sucessores para Grade de Ocupação
class WeightSearch:
    def __init__(self, grid, nx, ny):
        self.grid = grid
        self.dim_x = nx
        self.dim_y = ny
    
    def sucessores(self, atual):
        f = []
        x = atual[0]
        y = atual[1]
        
        if y + 1 != self.dim_y:
            if self.grid[x][y + 1] == 0:
                linha = []
                linha.append(x)
                linha.append(y + 1)
                custo = 1
                linha.append(custo)
                f.append(linha)
                
        if x + 1 != self.dim_x:
            if self.grid[x + 1][y] == 0:
                linha = []
                linha.append(x + 1)
                linha.append(y)
                custo = 3
                linha.append(custo)
                f.append(linha)
        
        if x - 1 >= 0:
            if self.grid[x - 1][y] == 0:
                linha = []
                linha.append(x - 1)
                linha.append(y)
                custo = 2
                linha.append(custo)
                f.append(linha)
        
        if y - 1 >= 0:
            if self.grid[x][y - 1] == 0:
                linha = []
                linha.append(x)
                linha.append(y - 1)
                custo = 4
                linha.append(custo)
                f.append(linha)
                
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
    
    def uniformCost(self, start, end): # Uniform Cost Search -> Working
        l1 = listaDEnc()
        l2 = listaDEnc()
        visitado = []
        l1.insereUltimo(start, 0, 0, None)
        l2.insereUltimo(start, 0, 0, None)
        linha = []
        linha.append(start)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if tuple(atual.estado) == tuple(end):
                path = []
                path = l2.exibeCaminho2(atual.estado, atual.v1)
                
                return path, atual.v2
        
            filhos = self.sucessores(atual.estado)
            
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.v2 + novo[2]  # custo do caminho
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
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                    
        return []  
    
    def greedySearch(self, inicio, fim): # Greedy Search -> Working
        l1 = listaDEnc()
        l2 = listaDEnc()
        visitado = []
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if tuple(atual.estado) == tuple(fim):
                print("Entrando no estado de fim")
                
                caminho = []
                caminho = l2.exibeCaminho2(atual.estado, atual.v1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                return caminho, atual.v2
        
            filhos = self.sucessores(atual.estado)            
            for novo in filhos:
                valor = (novo[0], novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.v2 + novo[2]  # custo do caminho
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
                            l1.inserePos_X(valor, v1, v2, atual)
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    if flag2:
                        visitado.append([valor, v2])
                        
        print("Caminho não encontrado")
        return [], 0
    
    def a_estrela(self, inicio, fim):
        l1 = listaDEnc()
        l2 = listaDEnc()
        visitado = []
        
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        
        linha = []
        linha.append(inicio)
        linha.append(0)
        
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            # print(atual.estado, atual.v2)
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeCaminho1(atual.estado, atual.v1)
                return caminho, atual.v2
        
            filhos = self.sucessores(atual.estado)
            
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.v2 + novo[2]  # custo do caminho
                #print("V2: ", v2);
                v1 = v2 + self.h(valor, fim) # f3(n)

                flag1 = True
                flag2 = True
                
                for j in range(len(visitado)):
                    print('Visitado: ', visitado[j][0])
                    print('Valor: ', valor)
                    print('V2:', v2)
                    if visitado[j][0][0] == valor[0] and visitado[j][0][1] == valor[1]:
                        if visitado[j][1] <= v2:
                            flag1 = False
                        else:
                            visitado[j][1] = v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(valor, v1, v2, atual)
                    l2.insereUltimo(valor, v1, v2, atual)
                    
                    if flag2:
                        linha = []
                        linha.append(valor)
                        linha.append(v2)
                        visitado.append(linha)
                        
        print("Não foi possível encontrar o caminho")
        return []

    def aia_estrela(self, inicio, fim, limite):  
        
        while True:
            lim_exc = []
            l1 = listaDEnc()
            l2 = listaDEnc()
            visitado = []
            l1.insereUltimo(inicio, 0, 0, None)
            l2.insereUltimo(inicio, 0, 0, None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() == False:
                atual = l1.deletaPrimeiro()
                
                if atual.estado == fim:
                    caminho = []
                    caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                    #print("Cópia da árvore:\n",l2.exibeLista())
                    #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")
                    return caminho, atual.valor2
            
                filhos = self.sucessores(atual.estado)
                
                for novo in filhos:
                    valor = []
                    valor.append(novo[0])
                    valor.append(novo[1])
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[2]  # custo do caminho
                    v1 = v2 + self.h(valor,fim) # f3(n)
                    if v1<=limite:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==valor:
                                if visitado[j][1]<=v2:
                                    flag1 = False
                                else:
                                    visitado[j][1]=v2
                                    flag2 = False
                                break
        
                        if flag1:
                            l1.inserePos_X(valor, v1, v2, atual)
                            l2.insereUltimo(valor, v1, v2, atual)
                            if flag2:
                                linha = []
                                linha.append(valor)
                                linha.append(v2)
                                visitado.append(linha)
                    else:
                        lim_exc.append(v1)
            limite = float(sum(lim_exc)/len(lim_exc))
            
        return []