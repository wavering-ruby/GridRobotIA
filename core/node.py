class Node(object):
    def __init__(self, parent = None, state = None, v1 = None, v2 = None, previous = None, next = None):
        self.parent    = parent
        self.state     = state
        self.v1        = v1  # Typically represents priority/f-score in search algorithms
        self.v2        = v2  # Typically represents path cost/g-score in search algorithms
        self.previous  = previous
        self.next      = next