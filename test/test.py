import random as rd
import funcoes_auxiliares1 as fa


class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, 
                valor2=None, anterior=None, proximo=None):
        # controle da árvore de busca
        self.pai       = pai
        # indica o nó do grafo
        self.estado    = estado
        # função de avaliação f(n) do método
        self.valor1    = valor1        
        # custo do caminho da origem até o nó atual
        self.valor2    = valor2     
        # controle da lista encadeada
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NA LISTA MANTENDO A ORDENAÇÃO
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):
    
    def custo_uniforme(self,inicio,fim,mapa,dim_x,dim_y):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
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
        
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
            #print(filhos)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  # custo do caminho
                v1 = v2 # f1(n)

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
                    
        return "Caminho não encontrado"      
    
    def greedy(self,inicio,fim,mapa,dim_x,dim_y):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
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
        
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  # custo do caminho
                v1 = fa.h(valor,fim) # f2(n)

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
                    
        return "Caminho não encontrado"
    
    def a_estrela(self,inicio,fim,mapa,dim_x,dim_y):  
        l1 = lista()
        l2 = lista()
        visitado = []
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
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
        
            filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
            for novo in filhos:
                valor = []
                valor.append(novo[0])
                valor.append(novo[1])
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[2]  # custo do caminho
                v1 = v2 + fa.h(valor,fim) # f3(n)

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
                    
        return "Caminho não encontrado"

    def aia_estrela(self,inicio,fim,mapa,dim_x,dim_y,limite):  
        
        while True:
            lim_exc = []
            l1 = lista()
            l2 = lista()
            visitado = []
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
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
            
                filhos = fa.sucessores(atual.estado,mapa,dim_x,dim_y)
                
                for novo in filhos:
                    valor = []
                    valor.append(novo[0])
                    valor.append(novo[1])
                    # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                    v2 = atual.valor2 + novo[2]  # custo do caminho
                    v1 = v2 + fa.h(valor,fim) # f3(n)
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
        return "Caminho não encontrado"

# HEURISTICA SERVE SOMENTE PARA DESTINO BUCARESTE
sol = busca()
caminho = []

# PROBLEMA C
mapa, dim_x, dim_y = fa.Gera_Ambiente('mapa.txt')
#print(mapa)

sol = busca()
caminho = []

# define ponto inicial
inicio = [0,0]

# define ponto final aleatoriamente
while True:
    x = rd.randrange(dim_x)
    y = rd.randrange(dim_y)
    if mapa[x][y]==1:
        break
    
final = [5, 5]
final.append(x)
final.append(y)

caminho, custo = sol.custo_uniforme(inicio,final,mapa,dim_x,dim_y)
print("Custo Uniforme: ",caminho[::-1],"\nCusto do Caminho: ",custo)

caminho, custo = sol.greedy(inicio,final,mapa,dim_x,dim_y)
print("\nGreedy: ",caminho[::-1],"\nCusto do caminho: ",custo)

caminho, custo = sol.a_estrela(inicio,final,mapa,dim_x,dim_y)
print("\nA_estrela: ",caminho[::-1],"\nCusto do caminho: ",custo)

limite = fa.h(inicio,final)
caminho, custo = sol.aia_estrela(inicio,final,mapa,dim_x,dim_y,limite)
print("\nAIA_estrela: ",caminho[::1],"\nCusto do caminho: ",custo)