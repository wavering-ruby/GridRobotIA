from LinkedList import listaDEnc

class buscaGridNP(object):
    
    # SUCESSORES PARA GRID (LISTA DE ADJACENCIAS)
    def sucessores(self,st,nx,ny,mapa):
        
        f = []
        x = st[0]
        y = st[1]
        
        # ABAIXO
        if x+1<nx:
            if mapa[x+1][y]==0:
                suc = []
                suc.append(x+1)
                suc.append(y)
                f.append(suc)
        
        # ACIMA
        if x-1>=0:
            if mapa[x-1][y]==0:
                suc = []
                suc.append(x-1)
                suc.append(y)
                f.append(suc)
        
        # DIREITA
        if y+1<ny:
            if mapa[x][y+1]==0:
                suc = []
                suc.append(x)
                suc.append(y+1)
                f.append(suc)
        
        # ESQUERDA
        if y-1>=0:
            if mapa[x][y-1]==0:
                suc = []
                suc.append(x)
                suc.append(y-1)
                f.append(suc)
        
        # DIAGONAL INFERIOR DIREITA
        if x+1<nx and y+1<ny:
            if mapa[x+1][y+1]==0:
                suc = []
                suc.append(x+1)
                suc.append(y+1)
                f.append(suc)
        
        # DIAGONAL INFERIOR ESQUERDA
        if x+1<nx and y-1>=0:
            if mapa[x+1][y-1]==0:
                suc = []
                suc.append(x+1)
                suc.append(y-1)
                f.append(suc)
        
        # DIAGONAL SUPERIOR DIREITA
        if x-1>=0 and y+1<ny:
            if mapa[x-1][y+1]==0:
                suc = []
                suc.append(x-1)
                suc.append(y+1)
                f.append(suc)
        
        # DIAGONAL SUPERIOR ESQUERDA
        if x-1>=0 and y-1>=0:
            if mapa[x-1][y-1]==0:
                suc = []
                suc.append(x-1)
                suc.append(y-1)
                f.append(suc)
                
        return f
#------------------------------------------------------------------------------    
    # CONTROLE DE NÓS REPETIDOS
    def verificaVisitado(self,novo,nivel,visitado):
        flag = True
        # controle de nós repetidos
        for aux in visitado:
            if aux[0]==novo:
                if aux[1]<=(nivel+1):
                    flag = False
                else:
                    aux[1]=nivel+1
                break
        return flag
#------------------------------------------------------------------------------
    # BUSCA EM AMPLITUDE
    def amplitude(self,inicio,fim,nx,ny,mapa):

        # manipular a FILA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            
            filhos = self.sucessores(atual.estado,nx,ny,mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo,atual.v1,visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo,atual.v1+1,0,atual)
                    l2.insereUltimo(novo,atual.v1+1,0,atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
#------------------------------------------------------------------------------
    # BUSCA EM PROFUNDIDADE
    def profundidade(self,inicio,fim,nx,ny,mapa):
        # manipular a PILHA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()
            
            filhos = self.sucessores(atual.estado,nx,ny,mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo,atual.v1,visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo,atual.v1+1,0,atual)
                    l2.insereUltimo(novo,atual.v1+1,0,atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
#------------------------------------------------------------------------------
    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self,inicio,fim,nx,ny,mapa,lim):
        # manipular a PILHA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()
            if atual.v1<lim:
                filhos = self.sucessores(atual.estado,nx,ny,mapa)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
    
                    # verifica se foi visitado
                    flag = self.verificaVisitado(novo,atual.v1,visitado)
    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo,atual.v1+1,0,atual)
                        l2.insereUltimo(novo,atual.v1+1,0,atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("\nFila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho

        return None    
    # BUSCA EM APROFUDAMENTO ITERATIVO
    def aprof_iterativo(self,inicio,fim,nx,ny,mapa,l_max):
        for lim in range(1,l_max):
            # manipular a PILHA para a busca
            l1 = listaDEnc()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = listaDEnc()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while l1.vazio() == False:
                # remove o último da PILHA
                atual = l1.deletaUltimo()
                if atual.v1<lim:
                    filhos = self.sucessores(atual.estado,nx,ny,mapa)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in filhos:
        
                        # verifica se foi visitado
                        flag = self.verificaVisitado(novo,atual.v1,visitado)
        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo,atual.v1+1,0,atual)
                            l2.insereUltimo(novo,atual.v1+1,0,atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.v1+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("\nFila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho

        return None    
#------------------------------------------------------------------------------
    # BUSCA BIDIRECIONAL
    def bidirecional(self,inicio,fim,nx,ny,mapa):
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = listaDEnc()
        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()
        
        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = listaDEnc()
        # cópia para apresentar o caminho (somente inserção)
        l4 = listaDEnc()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        
        l3.insereUltimo(fim,0,0,None)
        l4.insereUltimo(fim,0,0,None)
        
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!=l1.primeiro().v1:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
        
                filhos = self.sucessores(atual.estado,nx,ny,mapa)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo,atual.v1+1,visitado1)
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo,atual.v1+1,0,atual)
                        l2.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = not(self.verificaVisitado(novo,atual.v1+1,visitado2))
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!= l3.primeiro().v1:
                    break
                
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
        
                filhos = self.sucessores(atual.estado,nx,ny,mapa)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo,atual.v1+1,visitado2)
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo,atual.v1+1,0,atual)
                        l4.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = not(self.verificaVisitado(novo,atual.v1+1,visitado1))
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return "caminho não encontrado"