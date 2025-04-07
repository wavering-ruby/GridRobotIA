from Node import Node

class listaDEnc:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserePrimeiro(self, st, v1, v2, p):
        novo_no = Node(p, st, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    def insereUltimo(self, st, v1, v2, p):
        novo_no = Node(p, st, v1, v2, None, None)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
            self.tail = novo_no

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

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

    def vazio(self):
        return self.head is None
        
    def exibeLista(self):
        aux = self.head
        str1 = []
        while aux != None:
            temp = [aux.estado, aux.v1]
            if aux.pai != None:
                temp.append(aux.pai.estado)
            else:
                temp.append("nó raiz")
            str1.append(temp)
            aux = aux.proximo
        return str1
    
    def exibeCaminho(self):
        atual = self.tail
        path = []
        while atual.pai is not None:
            path.append(atual.estado)
            atual = atual.pai
        path.append(atual.estado)
        return path[::-1]
    
    def exibeCaminho1(self, valor):
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