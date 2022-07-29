# __add__ is called automatically when we try to add our <alredy made object>
# Add takes two argument

# 'self' is for first argument and 'other' is for second argument
# 'self' is right side of addition and 'other' is left side of addition

# it can't return string concatinaton..


class car:
    def __init__(self,size,color):
        self.size = size
        self.color = color
    
    def __add__(self,other):
        return self.color + other.color and self.size + other.size
        
        
        
c1 = car(10,"red")
c2 = car(12,"yellow")

print(c1 + c2)
    
    
