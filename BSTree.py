        self.leftchild = None
        self.rightchild = None
        
class Binary(object):
    def __init__(self):
        self.rootnode = None
    
    def insert_data(self, data):
        if not self.rootnode:
            self.rootnode = Node(data)
            
        else:
            self.insert_node(data, self.rootnode)
            
    def insert_node(self, data, node):
        if data < node.data:
            if not node.leftchild:
                node.leftchild = Node(data)
            else:
                self.insert_node(data, node.leftchild)
                
        else:
            if not node.rightchild:
                node.rightchild = Node(data)
            
            else:
                self.insert_node(data, node.rightchild)
                
        
    def get_min_val(self):
        if self.rootnode:
            return self.get_min(self.rootnode)
        
    
    def get_min(self, node):
        if node.leftchild:
            return self.get_min(node.leftchild)
        return node.data
    
    
    def get_max_value(self):
        if self.rootnode:
            return self.get_max(self.rootnode)
        
    def get_max(self, node):
        if node.rightchild:
            return get_max(node.rightchild)
        return node.data
        
    def tranversing(self):
        if self.rootnode:
            self.traverseInOrder(self.rootnode)
        
    def traverseInOrder(self, node):
        if node.leftchild:
            self.traverseInOrder(node.leftchild)
            
        print("%s "% node.data)
        
        
        if node.rightchild:
            self.traverseInOrder(node.rightchild)
