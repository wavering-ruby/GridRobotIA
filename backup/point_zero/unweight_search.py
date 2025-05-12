from .linked_list import LinkedList

class UnweightedSearch:
    def __init__(self, grid, nx, ny):
        self.grid = grid
        self.nx = nx
        self.ny = ny

    def gridSuccessors(self, state):
        """Generates valid successors for a state"""
        x, y = state
        moves = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),           # Cardinal movements
            (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)  # Diagonal movements
        ]
        validMoves = []
        
        for new_x, new_y in moves:
            if 0 <= new_x < self.nx and 0 <= new_y < self.ny and self.grid[new_x][new_y] == 0:
                validMoves.append([new_x, new_y])
        return validMoves

    def breadthFirstSearch(self, start_pos, end_pos):
        """
        Breadth-first search.
        Returns the found path or an empty list if no solution exists.
        """
        l1 = LinkedList()
        l2 = LinkedList()
        l1.insertLast(start_pos, 0, 0, None)
        l2.insertLast(start_pos, 0, 0, None)
        visited = [[start_pos, 0]]
        
        while not l1.empty():
            current = l1.deleteFirst()
            for new in self.gridSuccessors(current.state):
                flag = True
                for aux in visited:
                    if aux[0] == new:
                        if aux[1] <= (current.v1 + 1):
                            flag = False
                        else:
                            aux[1] = current.v1 + 1
                        break
                if flag:
                    l1.insertLast(new, current.v1 + 1, 0, current)
                    l2.insertLast(new, current.v1 + 1, 0, current)
                    visited.append([new, current.v1 + 1])
                    if new == list(end_pos):
                        return l2.displayPath()
        return []
    
    def depthFirstSearch(self, start_pos, end_pos):
        """
        Depth-first search.
        Returns the found path or an empty list if no solution exists.
        """
        stack = LinkedList()
        visited = set()
        stack.insertLast(start_pos, 0, 0, None)
        visited.add(tuple(start_pos))
        
        while not stack.empty():
            current = stack.deleteLast()
            
            
            if current.state == list(end_pos):
                path = []
                node = current
                
                
                while node is not None:
                    path.insert(0, node.state)
                    node = node.parent
                return path
            for neighbor in self.gridSuccessors(current.state):
                if tuple(neighbor) not in visited:
                    visited.add(tuple(neighbor))
                    stack.insertLast(neighbor, 0, 0, current)
        return []
    
    def checkVisited(self, new, level, visited):
        """
        Checks if node 'new' was already visited with a lower or equal level.
        If visited with a higher level, updates to the lower one.
        """
        flag = True
        
        for aux in visited:
            if aux[0] == new:
                if aux[1] <= (level + 1):
                    flag = False
                else:
                    aux[1] = level + 1
                break
        return flag

    def depthLimitedSearch(self, start_pos, end_pos, limit):
        """
        Depth-limited search.
        Returns the found path or None if the goal isn't reached.
        """
        l1 = LinkedList()  # For search
        l2 = LinkedList()  # To reconstruct the path
        l1.insertLast(start_pos, 0, 0, None)
        l2.insertLast(start_pos, 0, 0, None)
        visited = [[start_pos, 0]]
        
        while not l1.empty():
            current = l1.deleteLast()
            if current.v1 < limit:
                children = self.gridSuccessors(current.state)
                for new in children:
                    if self.checkVisited(new, current.v1, visited):
                        l1.insertLast(new, current.v1 + 1, 0, current)
                        l2.insertLast(new, current.v1 + 1, 0, current)
                        visited.append([new, current.v1 + 1])
                        if new == [end_pos[0], end_pos[1]]:
                            return l2.displayPath()
        return None

    def iterativeDeepeningSearch(self, start_pos, end_pos):
        """
        Iterative deepening search.
        Gradually increases the limit until finding a solution.
        Returns the found path or an empty list if no solution exists.
        """
        limit = 0
        while True:
            path = self.depthLimitedSearch(start_pos, end_pos, limit)
            
            if path:
                return path
            
            limit += 1
            
            if limit > self.nx * self.ny:  # Maximum limit (grid size)
                return []

    def bidirectionalSearch(self, start_pos, end_pos):
        """
        Bidirectional search.
        Performs search from both start and end simultaneously.
        Returns the found path or an empty list if no solution exists.
        """
        l1 = LinkedList()  # Search from start
        l2 = LinkedList()  # To reconstruct path (start)
        l3 = LinkedList()  # Search from end
        l4 = LinkedList()  # To reconstruct path (end)
        l1.insertLast(start_pos, 0, 0, None)
        l2.insertLast(start_pos, 0, 0, None)
        l3.insertLast(end_pos, 0, 0, None)
        l4.insertLast(end_pos, 0, 0, None)
        visited1 = [[start_pos, 0]]
        visited2 = [[end_pos, 0]]
        ni = 0
        
        while not l1.empty() or not l3.empty():
            while not l1.empty():
                if ni != l1.first().v1:
                    break
                
                current = l1.deleteFirst()
                children = self.gridSuccessors(current.state)
                
                for new in children:
                    if self.checkVisited(new, current.v1 + 1, visited1):
                        l1.insertLast(new, current.v1 + 1, 0, current)
                        l2.insertLast(new, current.v1 + 1, 0, current)
                        visited1.append([new, current.v1 + 1])
                        
                        if not self.checkVisited(new, current.v1 + 1, visited2):
                            path = [] + l2.displayPath() + l4.displayPath1(new)
                            return path
                        
            while not l3.empty():
                if ni != l3.first().v1:
                    break
                
                current = l3.deleteFirst()
                children = self.gridSuccessors(current.state)
                
                for new in children:
                    
                    if self.checkVisited(new, current.v1 + 1, visited2):
                        l3.insertLast(new, current.v1 + 1, 0, current)
                        l4.insertLast(new, current.v1 + 1, 0, current)
                        visited2.append([new, current.v1 + 1])
                        
                        if not self.checkVisited(new, current.v1 + 1, visited1):
                            path = [] + l4.displayPath() + l2.displayPath1(new)
                            return path[::-1]
            ni += 1
        return []