class car:
    def __init__(self,size,color):
        
        self.color = color
        self.size = size
    
    def __repr__(self):
        return "hi { }".format(self.color)   
        
c1 = car(10,"red")

print(c1)

    
    
