import sys
class Node(object):
    
    def __init__(self, name):
        
        self.name = name
        self.predecessor = None
        self.adjacency = []
        self.visited = False
        self.mindistance = self.maxsize
        
        
class Edge(object):
    
    def __init__(self, start, stop, weight):
        
        self.start = start
        self.stop = stop
        self.weight = weight
        
class bellmanford(object):
    
    Has_cycle = False
    
    def calculateEdges(self, targetlist, edgelist, weight):
    
        
        start.mindistance = 0
        
        for i in range (0, len(targetlist)-1):
            
            for edge in edgelist:
                
                u = edge.start
                
                v = edge.stop
                
                if u.mindistance + edge.weight < v.mindistance:
                    v.mindistance = u.mindistance+ edge.weight
                    v.predecessor = u
                    
                    
            for edge in edgelist:
                if self.hasloop(edge):
                    print("looop detected")
                    bellmanford.Has_cycle = True
                    return
                
    def hasloop(self, edge):
        if edge.start.mindistance + edge.weight < edge.stop.mindistance:
            return True
        
        else:
            return False
        
        
    def getdistance(self, target):
        
        if not bellmanford.hasloop:
            
            print("target vertex distance is  " +str(stop.mindistance))
            
            node = stop
            
            while not node:
                
                print("name of node is ", node.name)
                node = node.predecessor
                
            else:
                
                print("negative value detected")
                
            
                
                    
