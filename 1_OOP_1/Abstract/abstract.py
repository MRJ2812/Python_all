# We can't make object for this class

from abc import ABC,abstractmethod

class parent(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @abstractmethod                                 # It's crucial for perfect abstraction
    def calculate(self):
        pass
    



