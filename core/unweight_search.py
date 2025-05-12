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
    
    def checkVisited(self, new, level, visited):
        for node in visited:
            if node[0] == new and node[1] <= level:
                return False
        return True

    def breadthFirstSearch(self, start_pos, end_pos):
        self.path = []
        
        queue = LinkedList()
        path_copy = LinkedList()

        queue.insertLast(start_pos, 0, 0, None)
        path_copy.insertLast(start_pos, 0, 0, None)

        visited = []
        line = []
        line.append(start_pos)
        line.append(0)
        visited.append(line)

        while queue.empty() == False:
            current = queue.deleteFirst()
            
            children = self.gridSuccessors(current.state)

            for new in children:
                is_visited = self.checkVisited(new, current.v1 + 1, visited)
                
                if is_visited:
                    queue.insertLast(new, current.v1 + 1, 0, current)
                    path_copy.insertLast(new, current.v1 + 1, 0, current)

                    line = []
                    line.append(new)
                    line.append(current.v1 + 1)
                    visited.append(line)

                    target_pos = [end_pos[0], end_pos[1]]
                    
                    if new == target_pos:
                        path = []
                        path += path_copy.displayPath()
                        self.path = path
                        return self.path

        return None

    def depthFirstSearch(self, start_pos, end_pos):
        self.path = []
        
        stack = LinkedList()
        path_copy = LinkedList()

        stack.insertLast(start_pos, 0, 0, None)
        path_copy.insertLast(start_pos, 0, 0, None)

        visited = []
        line = []
        line.append(start_pos)
        line.append(0)
        visited.append(line)

        while stack.empty() == False:
            current = stack.deleteLast()
            
            children = self.gridSuccessors(current.state)
    
            for new in children:
                is_visited = self.checkVisited(new, current.v1 + 1, visited)
    
                if is_visited:
                    stack.insertLast(new, current.v1 + 1, 0, current)
                    path_copy.insertLast(new, current.v1 + 1, 0, current)
    
                    line = []
                    line.append(new)
                    line.append(current.v1 + 1)
                    visited.append(line)
                    
                    target_pos = [end_pos[0], end_pos[1]]
                    
                    if tuple(new) == tuple(target_pos):
                        path = []
                        path += path_copy.displayPath()
                        self.path = path
                        return self.path

        return None

    def depthLimitedSearch(self, start_pos, end_pos, limit):
        self.path = []
        
        stack = LinkedList()
        path_copy = LinkedList()

        stack.insertLast(start_pos, 0, 0, None)
        path_copy.insertLast(start_pos, 0, 0, None)

        visited = []
        line = []
        line.append(start_pos)
        line.append(0)
        visited.append(line)

        while stack.empty() == False:
            current = stack.deleteLast()
            
            if current.v1 < limit:
                children = self.gridSuccessors(current.state)
    
                for new in children:
                    is_visited = self.checkVisited(new, current.v1, visited)
    
                    if is_visited:
                        stack.insertLast(new, current.v1 + 1, 0, current)
                        path_copy.insertLast(new, current.v1 + 1, 0, current)
    
                        line = []
                        line.append(new)
                        line.append(current.v1 + 1)
                        visited.append(line)
                        
                        target_pos = [end_pos[0], end_pos[1]]
                        
                        if tuple(new) == tuple(target_pos):
                            path = []
                            path += path_copy.displayPath()
                            self.path = path
                            return self.path

        return None

    def iterativeDeepeningSearch(self, start_pos, end_pos):
        depth_limit = 0
        
        while True:
            path = self.depthLimitedSearch(start_pos, end_pos, depth_limit)
            
            if path:
                return path
            
            depth_limit += 1
            
            if depth_limit > self.nx * self.ny:
                return []
            
    def bidirectionalSearch(self, start_pos, end_pos):
        path = []
        
        queue1 = LinkedList()  # Busca do início
        path_copy1 = LinkedList()  # Cópia do caminho (início)
        
        queue2 = LinkedList()  # Busca do fim
        path_copy2 = LinkedList()  # Cópia do caminho (fim)
    
        queue1.insertLast(start_pos, 0, 0, None)
        path_copy1.insertLast(start_pos, 0, 0, None)
        
        queue2.insertLast(end_pos, 0, 0, None)
        path_copy2.insertLast(end_pos, 0, 0, None)
        
        visited1 = []
        line = []
        line.append(start_pos)
        line.append(0)
        visited1.append(line)
        
        visited2 = []
        line = []
        line.append(end_pos)
        line.append(0)
        visited2.append(line)
        
        current_depth = 0
        
        while queue1.empty() == False or queue2.empty() == False:
            
            while queue1.empty() == False:
                
                if current_depth != queue1.first().v1:
                    break
                    
                current = queue1.deleteFirst()
                children = self.gridSuccessors(current.state)
                
                for new in children:
                    is_visited = self.checkVisited(new, current.v1 + 1, visited1)
                    
                    if is_visited:
                        queue1.insertLast(new, current.v1 + 1, 0, current)
                        path_copy1.insertLast(new, current.v1 + 1, 0, current)
        
                        line = []
                        line.append(new)
                        line.append(current.v1 + 1)
                        visited1.append(line)
        
                        is_visited_other = not(self.checkVisited(new, current.v1 + 1, visited2))
                        
                        if is_visited_other:    
                            path = []
                            path += path_copy1.displayPath()
                            path += path_copy2.displayPath1(new)
                            return path
                        
            while queue2.empty() == False:
                
                if current_depth != queue2.first().v1:
                    break
                
                current = queue2.deleteFirst()
                children = self.gridSuccessors(current.state)
                
                for new in children:
                    is_visited = self.checkVisited(new, current.v1 + 1, visited2)
                    
                    if is_visited:
                        queue2.insertLast(new, current.v1 + 1, 0, current)
                        path_copy2.insertLast(new, current.v1 + 1, 0, current)
        
                        line = []
                        line.append(new)
                        line.append(current.v1 + 1)
                        visited2.append(line)
        
                        is_visited_other = not(self.checkVisited(new, current.v1 + 1, visited1))
                        
                        if is_visited_other:
                            path = []
                            path += path_copy2.displayPath()
                            path += path_copy1.displayPath1(new)
                            return path[::-1]
                            
            current_depth += 1

        return path