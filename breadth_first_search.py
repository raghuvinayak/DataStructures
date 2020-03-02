
class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.adjustancy = []
        self.visited = False
        
        
class BFS(object):
    
    def breadth4S(self, rootnode):
        
        queue = [] 
        queue.append(rootnode)
        rootnode.visited = True
        
        while queue:
            actualnode = queue.pop(0)
            print(actualnode.data)
           
            for n in actualnode.adjustancy:

                if not n.visited:
                    n.visited = True
                    queue.append(n)
