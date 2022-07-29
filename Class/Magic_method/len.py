# For  information , check add file.

class car:
    def __init__(self,size,color):
        self.size = size
        self.color = color
    
    def __len__(self):
        return len(self.color)
        
        
        
c1 = car(10,"red")
c2 = car(12,"yellow")

print(len(c1.color))      # red = 3
    
    
