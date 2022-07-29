# the class method is a method that can change the calss value....
# it return a value,,,and return goes to constructor   as perameter...
# We can manupulate data from outside call the class method

class student:
    def __init__(self,new):        # step 2
        self.new = new
        
    def display(self):
        return self.new

    @classmethod
    def change(cls):             #step 1
        return cls(20)

st = student(10)
print(st.display())


st = student.change()
print(st.display())

        

        