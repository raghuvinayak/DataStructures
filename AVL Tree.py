import sys
sys.setrecursionlimit(1500)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 0
        

class AVL(object):
    
    def __init__(self):
        self.rootnode = None
        
    def insert_data(self, data):
        
        self.rootnode = self.insert_node(data, self.rootnode)
            
    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftchild = self.insert_node(data, node.leftchild)
        else:
            node.rightchild = self.insert_node(data, node.rightchild)
            
        node.height = max(self.cal_height(node.leftchild), self.cal_height(node.rightchild))+1
        
        return self.settleviolation(data, node)
    
    
    def settleviolation(self, data, node):
        balance = self.cal_balance(node)
        
        #case 1 LL
        if balance > 1 and data < node.leftchild.data:
            print("left left heavy sistuation..........", node.data)
            return self.rotate_Right(node)
        
        #case 2 RR
        if balance < -1 and data  > node.rightchild.data:
            print("right right heavy sistuation.......", node.data)
            return self.rotate_Left(node)
        
        #case 3 RL
        if balance < -1 and data < node.rightchild.data:
            print(" right left heavy sistuation.........", node.data)
            node.rightchild =  self.rotate_Right(node.rightchild)
            return self.rotate_Left(node)
        
        #case 4 LR
        if balance > 1 and data > node.leftchild.data:
            print("left right heavy sistuation.......", node.data)
            node.leftchild = self.rotate_Left(node.leftchild)
            return self.rotate_Right(node)
        
        return node
    
    def traversing(self):
        if self.rootnode:
            return self.travesing_data(self.rootnode) 
            
    def travesing_data(self, node):
        if node.leftchild:
            self.travesing_data(node.leftchild)
            
        print(node.data)
            
        if node.rightchild:
            self.travesing_data(node.rightchild)
            

    
    def remove(self, data):
        if self.rootnode:
            self.rootnode = self.removenode(data, self.rootnode)
            
    def removenode(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.leftchild = self.removenode(data, node.leftchild)
        elif data > node.data:
            node.rightchild = self.removenode(data, node.rightchild)
            
        else:
            if not node.leftchild and not node.rightchild:
                print("removing leaf node......", node.data)
                del node
                return None
            
            if not node.leftchild:
                print("removing the a node on right child.....", node.data)
                newnode = node.rightchild
                del node
                return newnode
            
            elif not node.rightchild:
                print("removing the node on left child......", node.data)
                newnode = node.leftchild
                del node
                return newnode
            print("removing node with two child")
            tempnode = self.getPredecessor(node.leftchild)
            node.data = tempnode.data
            node.leftchild = self.removenode(tempnode.data, node.leftchild)
        
        if not node:
            return node
        
        node.height = max( self.cal_height(node.leftchild), self.cal_height(node.rightchild)) + 1
        return self.settleviolation(data, node)
        return node
            
            
    def getPredecessor(self, node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
            
        return node   
                                             
    def cal_height(self, node):
        if not node:
            return -1
        return node.height
    
    def cal_balance(self, node):
        if not node:
            return 0
        return self.cal_height(node.leftchild) - self.cal_height(node.rightchild)
    
    def rotate_Right(self, node):
        tempLeftchild = node.leftchild
        node.leftchild = node.leftchild.rightchild
        tempLeftchild.rightchild = node
      
        
        node.height = max( self.cal_height(node.leftchild), self.cal_height(node.rightchild)) + 1
        tempLeftchild.height = max( self.cal_height(tempLeftchild.leftchild), self.cal_height(tempLeftchild.rightchild)) + 1
        return tempLeftchild
    
    def rotate_Left(self, node):
        tempRightchild = node.rightchild
        node.rightchild = node.rightchild.leftchild
        tempRightchild.leftchild = node       
        node.height = max( self.cal_height(node.leftchild), self.cal_height(node.rightchild)) + 1
        tempRightchild.height = max( self.cal_height(tempRightchild.leftchild), self.cal_height(tempRightchild.rightchild)) + 1
        return tempRightchild
        
  
    
