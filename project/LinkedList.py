from Node import Node

class listaDEnc(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, v1, v2, p):
        novo_no = Node(p, st, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, v1, v2, p):

        novo_no = Node(p, st, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
            self.tail = novo_no

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

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head
    
    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):
        
        aux = self.head
        str1 = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.v1)
            if aux.pai!=None:
                temp.append((aux.pai).estado)
            else:
                temp.append("nó raiz")
            str1.append(temp)
            aux = aux.proximo
        
        return str1
    
    # EXIBE O CAMINHO ENCONTRADO
    def ShowPath(self):
        
        atual = self.tail
        
        path = []
        
        while atual.pai is not None:
            path.append(atual.estado)
            atual = atual.pai
            
        path.append(atual.estado)
        
        path = path[::-1]
        
        return path
    
    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def ShowPath2(self, valor):
                
        atual = self.head
        
        while atual.estado != valor:
            atual = atual.proximo
    
        path = []
        
        atual = atual.pai
        
        while atual.pai is not None:
            path.append(atual.estado)
            atual = atual.pai
            
        path.append(atual.estado)
        
        return path