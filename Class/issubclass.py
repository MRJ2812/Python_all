'''Chcek subclass'''

class A:
    def display_1(self):
        print("This is A class")
        
class B(A):
     def display_2(self):
        print("This is B class")
        
class C(B):
     def display_3(self):
        print("This is A class")
        
c = C()

print(issubclass(C, A))     # Check if C is is subclass of A