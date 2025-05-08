from .linked_list import LinkedList
from math import sqrt

# Successor routine for Occupancy Grid
class WeightedSearch:
    def __init__(self, grid, nx, ny):
        self.grid = grid
        self.dim_x = nx
        self.dim_y = ny
    
    def getSuccessors(self, current):
        successors = []
        x = current[0]
        y = current[1]
        
        if y + 1 != self.dim_y:
            if self.grid[x][y + 1] == 0:
                successor = []
                successor.append(x)
                successor.append(y + 1)
                cost = 1
                successor.append(cost)
                successors.append(successor)
                
        if x + 1 != self.dim_x:
            if self.grid[x + 1][y] == 0:
                successor = []
                successor.append(x + 1)
                successor.append(y)
                cost = 3
                successor.append(cost)
                successors.append(successor)
        
        if x - 1 >= 0:
            if self.grid[x - 1][y] == 0:
                successor = []
                successor.append(x - 1)
                successor.append(y)
                cost = 2
                successor.append(cost)
                successors.append(successor)
        
        if y - 1 >= 0:
            if self.grid[x][y - 1] == 0:
                successor = []
                successor.append(x)
                successor.append(y - 1)
                cost = 4
                successor.append(cost)
                successors.append(successor)
                
        return successors
    
    @staticmethod
    def heuristic(p1, p2):
        if p1[0] < p2[0]:
            m1 = 3  # action cost from successor routine
        else:
            m1 = 2  # action cost from successor routine
        
        if p1[1] < p2[1]:
            m2 = 1  # action cost from successor routine
        else:
            m2 = 4  # action cost from successor routine
        
        # Heuristic WITHOUT diagonal movement
        # h = abs(p1[0] - p2[0]) * m1 + abs(p1[1] - p2[1]) * m2
        # Heuristic WITH diagonal movement
        h = sqrt(m1 * (p1[0] - p2[0]) * (p1[0] - p2[0]) + m2 * (p1[1] - p2[1]) * (p1[1] - p2[1]))
        
        return h
    
    def uniformCostSearch(self, start, end):  # Uniform Cost Search -> Working
        frontier = LinkedList()
        path_nodes = LinkedList()
        visited = []
        frontier.insertLast(start, 0, 0, None)
        path_nodes.insertLast(start, 0, 0, None)
        entry = []
        entry.append(start)
        entry.append(0)
        visited.append(entry)
        
        while frontier.empty() == False:
            current = frontier.deleteFirst()
            
            if tuple(current.state) == tuple(end):
                path = path_nodes.displayPath2(current.state, current.v1)
                return path, current.v2
        
            successors = self.getSuccessors(current.state)
            
            for successor in successors:
                position = []
                position.append(successor[0])
                position.append(successor[1])
                
                # CALCULATE COST FROM ORIGIN TO CURRENT NODE
                path_cost = current.v2 + successor[2]  # path cost
                priority = path_cost  # f1(n)

                should_add = True
                should_update = True
                
                for entry in visited:
                    if entry[0] == position:
                        if entry[1] <= path_cost:
                            should_add = False
                        else:
                            entry[1] = path_cost
                            should_update = False
                        break

                if should_add:
                    frontier.insertPos_X(position, priority, path_cost, current)
                    path_nodes.insertLast(position, priority, path_cost, current)
                    if should_update:
                        new_entry = []
                        new_entry.append(position)
                        new_entry.append(path_cost)
                        visited.append(new_entry)
                    
        return [], current.v2
    
    def greedySearch(self, start, end):  # Greedy Search -> Working
        frontier = LinkedList()
        path_nodes = LinkedList()
        visited = []
        frontier.insertLast(start, 0, 0, None)
        path_nodes.insertLast(start, 0, 0, None)
        entry = []
        entry.append(start)
        entry.append(0)
        visited.append(entry)
        
        while frontier.empty() == False:
            current = frontier.deleteFirst()
            
            if tuple(current.state) == tuple(end):
                path = path_nodes.displayPath2(current.state, current.v1)
                return path, current.v2
        
            successors = self.getSuccessors(current.state)            
            for successor in successors:
                position = (successor[0], successor[1])
                
                # CALCULATE COST FROM ORIGIN TO CURRENT NODE
                path_cost = current.v2 + successor[2]  # path cost
                priority = self.heuristic(position, end)  # f2(n)
                
                should_add = True
                should_update = True
                for entry in visited:
                    if entry[0] == position:
                        if entry[1] <= path_cost:
                            should_add = False
                        else:
                            entry[1] = path_cost
                            should_update = False
                            frontier.insertPos_X(position, priority, path_cost, current)
                        break

                if should_add:
                    frontier.insertPos_X(position, priority, path_cost, current)
                    path_nodes.insertLast(position, priority, path_cost, current)
                    if should_update:
                        visited.append([position, path_cost])
                        
        return [], 0
    
    def aStarSearch(self, start, end):  # A* Search -> Working
        frontier = LinkedList()
        path_nodes = LinkedList()
        visited = []
        
        frontier.insertLast(start, 0, 0, None)
        path_nodes.insertLast(start, 0, 0, None)
        
        entry = []
        entry.append(start)
        entry.append(0)
        
        visited.append(entry)
        
        while frontier.empty() == False:
            current = frontier.deleteFirst()
            
            if tuple(current.state) == tuple(end):
                path = path_nodes.displayPath2(current.state, current.v1)
                return path, current.v2
        
            successors = self.getSuccessors(current.state)
            
            for successor in successors:
                position = []
                position.append(successor[0])
                position.append(successor[1])
                
                # CALCULATE COST FROM ORIGIN TO CURRENT NODE
                path_cost = current.v2 + successor[2]  # path cost
                priority = path_cost + self.heuristic(position, end)  # f3(n)

                should_add = True
                should_update = True
                
                for entry in visited:
                    if entry[0][0] == position[0] and entry[0][1] == position[1]:
                        if entry[1] <= path_cost:
                            should_add = False
                        else:
                            entry[1] = path_cost
                            should_update = False
                        break

                if should_add:
                    frontier.insertPos_X(position, priority, path_cost, current)
                    path_nodes.insertLast(position, priority, path_cost, current)
                    
                    if should_update:
                        new_entry = []
                        new_entry.append(position)
                        new_entry.append(path_cost)
                        visited.append(new_entry)
                        
        return [], 0

    def aaiStarSearch(self, start, end, limit):  # aai* Search -> Working
        while True:
            exceeded_limits = []
            frontier = LinkedList()
            path_nodes = LinkedList()
            visited = []
            frontier.insertLast(start, 0, 0, None)
            path_nodes.insertLast(start, 0, 0, None)
            entry = []
            entry.append(start)
            entry.append(0)
            visited.append(entry)
            
            while frontier.empty() == False:
                current = frontier.deleteFirst()
                
                if tuple(current.state) == tuple(end):
                    path = path_nodes.displayPath2(current.state, current.v1)
                    return path, current.v2
            
                successors = self.getSuccessors(current.state)
                
                for successor in successors:
                    position = []
                    position.append(successor[0])
                    position.append(successor[1])
                    
                    # CALCULATE COST FROM ORIGIN TO CURRENT NODE
                    path_cost = current.v2 + successor[2]  # path cost
                    priority = path_cost + self.heuristic(position, end)  # f3(n)
                    if priority <= limit:
                        should_add = True
                        should_update = True
                        for entry in visited:
                            if entry[0] == position:
                                if entry[1] <= path_cost:
                                    should_add = False
                                else:
                                    entry[1] = path_cost
                                    should_update = False
                                break
        
                        if should_add:
                            frontier.insertPos_X(position, priority, path_cost, current)
                            path_nodes.insertLast(position, priority, path_cost, current)
                            if should_update:
                                new_entry = []
                                new_entry.append(position)
                                new_entry.append(path_cost)
                                visited.append(new_entry)
                    else:
                        exceeded_limits.append(priority)
                        
            if not exceeded_limits:
                return [], 9999
            else:
                limit = sum(exceeded_limits) / len(exceeded_limits)