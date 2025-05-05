from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, st, v1, v2, p):
        new_node = Node(p, st, v1, v2, None, None)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
        self.head = new_node
            
    def insertPos_X(self, s, v1, v2, p):
        # if list is empty
        if self.head is None:
            self.insertFirst(s,v1,v2,p)
        else:
            current = self.head
            while current.v1 < v1:
                current = current.next
                if current is None: break
            
            if current == self.head:
                self.insertFirst(s,v1,v2,p)
            else:
                if current is None:
                    self.insertLast(s,v1,v2,p)
                else:
                    new_node = Node(p,s,v1,v2,None,None)
                    aux = current.previous
                    aux.next = new_node
                    new_node.previous = aux
                    current.previous = new_node
                    new_node.next = current

    def insertLast(self, st, v1, v2, p):
        new_node = Node(p, st, v1, v2, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
        self.tail = new_node

    def deleteFirst(self):
        if self.head is None:
            return None
        else:
            node = self.head
            
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
            return node

    def deleteLast(self):
        if self.tail is None:
            return None
        else:
            node = self.tail
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            return node

    def first(self):
        return self.head
    
    def last(self):
        return self.tail

    def empty(self):
        return self.head is None
        
    def displayList(self):
        aux = self.head
        str = []
        while aux != None:
            temp = [aux.state, aux.v1]
            if aux.parent != None:
                temp.append(aux.parent.state)
            else:
                temp.append("root node")
            str.append(temp)
            aux = aux.next
        return str
    
    def displayPath(self):
        current = self.tail
        path = []
        
        while current.parent is not None:
            path.append(current.state)
            current = current.parent
            
        path.append(current.state)
        return path[::-1]
    
    def displayPath1(self, value):
        current = self.head
        
        while current.state != value:
            current = current.next
        path = []
        current = current.parent
        while current.parent is not None:
            path.append(current.state)
            current = current.parent
        path.append(current.state)
        return path
    
    def displayPath2(self, s, v1):
        current = self.tail
        
        while current.state != s or current.v1 != v1:
            current = current.previous
        
        path = []
        
        while current.parent is not None:
            path.append(current.state)
            current = current.parent
        
        path.append(current.state)
        
        return path[::-1]