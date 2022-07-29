# We use constructor cause it helps us to inithialize vaiable only one time with class__object....  
# When you create a class ,, create a constructor then do other thing

class student:
    
    def __init__(self,name,Roll):
        self.name = name
        self.Roll = Roll
        self.email = name + "gmail.com"              # We can make new attribute without calling
        
    def display(self):
        print(f"Name {self.name} and Roll {self.Roll} and {self.email} ")
        
st = student('joy', 463)
st.display()
