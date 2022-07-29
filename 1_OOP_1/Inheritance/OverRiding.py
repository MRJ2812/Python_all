# same method used in child class and only child calss method work
# it called method Overridding

class parent:
    def __init__(self):
        print("hi i am parent")


class child(parent):
    def __init__(self):
       print("hi i am child")
       

    
        

ch = child()