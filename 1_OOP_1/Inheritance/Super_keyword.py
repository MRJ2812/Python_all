#super keyword called parent class method

class parent:
    def __init__(self):
        print("hi i am parent")


class child(parent):
    def __init__(self):
       print("hi i am child")
       super().__init__()                    # This is super keyword.
       

    
        

ch = child()