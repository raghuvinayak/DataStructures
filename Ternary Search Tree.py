class Node(object):
    
    def __init__(self, character):
        self.character = character
        self.leftnode = None
        self.rightnode = None
        self.middlenode = None
        self.value = 0
        
class TNT(object):
    
    def __init__(self):
        self.rootnode = None
        
    def put(self, key, value):
        self.rootnode = self.put_item(self.rootnode, key, value, 0)
        
    def put_item(self, node, key, value, index):
        char = key[index]
        
        if node == None:
            node =  Node(char)
        
        if char < node.character:
            node.leftnode = self.put_item(node.leftnode, key, value, index)
        
        elif char > node.character:
            node.rightnode = self.put_item(node.rightnode, key, value, index)
            
        elif index < len(key)-1:
            node.middlenode = self.put_item(node.middlenode, key, value, index +1)
            
        else:
            node.value = value
            
        return node
            
            
    def get(self, key):
        node =  self.get_item(self.rootnode, key, 0)
        
        if node == None:
            return -1
        return node.value
    
    def get_item(self, node, key, index):
        
        if node == None:
            return None
        
        c = key[index]
        
        if c < node.character:
            return self.get_item(node.leftnode, key, index)
        elif c > node.character:
            return self.get_item(node.rightnode, key, index)
        
        elif index < len(key)-1:
            return self.get_item(node.middlenode, key, index+1)
        
        else:
            return node
        

if __name__ == "__main__":
    test = TNT()
    
 
