#    A,B --> C

class A:
    def display_1(self):
        print("This is A class")
        
class B:
     def display_2(self):
        print("This is B class")
        
class C(A,B):
    pass
        
c = C()

c.display_1()
c.display_2()


# ------------------------- Another ----------------------------

class X:
    def display(self):
        print("This is X class")
        
class Y:
     def display(self):
        print("This is Y class")
        
class Z(X,Y):                            # (First priority , Second priority)
    pass
        
z = Z()

z.display()                              # (First priority , Second priority)
