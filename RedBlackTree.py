class NilNode(object):
   
    def __init__(self):
        self.red = False

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.red = False
        self.parent = None
        
class RedBlack(object):
    
    def __init__(self):
        self.rootnode = None
        
        
    def insert(self, data):
        if self.rootnode:
            node = Node(data)
            node.red = False
            self.rootnode = self.insertNode(data)
            return
        
        
    def insertNode(self, data, node):
        
        if not node:
            return Node(data)
        
        potential_parent = data
        print(potential_parent)
        if data < node.data:
             node.leftchild = self.insertNode(data, node.leftchild)


        else:
            node.rightchild = self.insertNode(data, node.rightchild)
        node.parent = potential_parent
        if node.parent <node.parent.data:
            node.parent.leftchild = node
        else:
            node.parent.rightchild= node
            
        return self.RedBlackFixing(node)          

    def RedBlackFixing(self, node):
        while node.parent.red == True and node != self.rootnode:

            if node.parent == node.parent.parent.leftchild:
                uncle_node = node.parent.parent.rightchild
                if uncle_node.red:
                    node.parent.red = False
                    node.uncle_node = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                    
                else:
                    if node.parent == node.parent.rightchild:
                        node = node.parent
                        self.rotateleft(node)
                    node.parent.red = False
                    node.parent.parent = True
                    return self.rotateright(node.parent.parent)
            else:
                uncle_node = node.parent.parent.leftchild
    
                if uncle_node.red:
                    node.parent.red = False
                    node.uncle_node = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                    
                else:
                    if node.parent == node.parent.leftchild:
                        node = node.parent
                        self.rotateright(node)
                    node.parent.red = False
                    node.parent.parent = True
                    return self.rotateleft(node.parent.parent)
                    
        self.rootnode.red = False
 
    
    def traversing(self):
        if self.rootnode:
            return self.travesing_data(self.rootnode) 
            
    def travesing_data(self, node):
        if node.leftchild:
            self.travesing_data(node.leftchild)
            
        print(node.data)
            
        if node.rightchild:
            self.travesing_data(node.rightchild)
            
    
                
    def rotateleft(self, node):
        print("Rotating left!")
        tempRightchild = node.rightchild
        node.rightchild = node.rightchild.leftchild
        tempRightchild.leftchild = node   
        return tempRightchild
    
    def rotateright(self, node):
        print("Rotating right!")
        tempLeftchild = node.leftchild
        node.leftchild = node.leftchild.rightchild
        tempLeftchild.rightchild = node
        return tempLeftchild
    
