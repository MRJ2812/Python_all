#  @function_Name   means  "new = update(functoin_Name)"

def update(func):
    def for_call_first_function():             # 3rd- This function called when it returns and into this
        print("*********")                     # functiona perameter function (old) call
        func()
        print("*******")
    return for_call_first_function              # Here the nested function not call.. it will call in 17 line



@update            # something = update(old)      # 2nd- it's is come here and see there are a decorator
def old():                                        # means this function went as perameter in update function 
    print("This is a old function")
    

old()                                              # 1st- we call old function

