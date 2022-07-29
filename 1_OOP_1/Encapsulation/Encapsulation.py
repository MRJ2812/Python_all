# This is a single class Encapculation..
# This is a way to get the data..


class employee:
    def __init__(self):
        self.name = "joy"
        self.__acNo = "2812"
        
        
        
em = employee()


print(em.name)
print(em.__acNo)
print(em._employee__acNo)   # this is called name mangling, This is for private function

    
    