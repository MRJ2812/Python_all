'''Private method can only access by public class'''
'''Private variable can only access by public class'''
# Underscore for make private 

class A:
        __private = 10                          # this is a private variable
        def __init__(self):
                self.__private = 10
            
        def __display(self):                    # This is a private method
                print(self.__private)
                
        def another_display(self):
            self.__display()                   
                
c = A()
c.another_display()