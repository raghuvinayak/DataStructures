class HashMap(object):
    
    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size
        
    def insert(self, key, data):
        index = self.hashing(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            index = (index+1)%self.size
        self.keys[index] = key
        self.values[index] = data
        
        
    def get(self, key):
        index = self.hashing(key)
        while self.keys[index] is not None:
            
            if self.keys[index] == key:
                return self.values[index]
            index = (index+1)% self.size
        
        return None
        
    
    
    def hashing(self, key):
        sum = 0
        for position in range(len(key)):
            sum = sum + ord(key[position])
        return sum%self.size
            
    
if __name__ == "__main__":
    table = HashMap()
    table.insert('apple',10)
    table.insert('iphont',11)
    table.insert('tommy',12)
    table.insert('pineapple',13)
    print(table.get('pineapple'))
