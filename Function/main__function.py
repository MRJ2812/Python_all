# 47 
# This is the main file 

def function1():
    return f"Hi I am function 1"

def function2(num1,num2):
    return num1+num2
 

# This is two normal function and we normally call them in this file.
# we also call those from another file named "main_function_2".
# If we call those function from this and also another file , they will print by both command.
# Try is ---> call from another function

# we use main which is works like main function in C ,, if we don't call it here it will
# not show in another file.

# See here a condition is ---> the value of name is main
# Only this file , name value is main ,, another file it's not main. 
    
if __name__ == '__main__':
    print(function1())

    print(function2(10,20))
    
    

