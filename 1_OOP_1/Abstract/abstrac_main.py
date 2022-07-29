from abstract import parent
 
class child(parent):
     
    def calculate(self):
         print(self.x + self.y)
    
c = child(10,20) 

c.calculate()