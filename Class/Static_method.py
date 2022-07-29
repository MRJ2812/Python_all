# Works like a normal method like java 
# we can give perameter if we want

class student:
    def __init__(self,new):        # step 2
        self.new = new
        
    def display(self):
        return self.new

    @staticmethod
    def change():             
        print("hi i do like a normal method like in java")

st = student.change()

