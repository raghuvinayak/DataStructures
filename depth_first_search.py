class Node(object):
    
    def __init__(self, name):
        
        self.name = name
        self.visited = False
        self.adjacency = []
        
        
class DepthFS(object):
    
    def dfs(self, rootnode):
        
        rootnode.visited = True
        print(rootnode.name)
        
        for n in rootnode.adjacency:
            if not n.visited:
                return self.dfs(n)
            
