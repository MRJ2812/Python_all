# It means a string line in a function first line
# There are a way to print doc_string

def docs():
    """This is a doc string""" 
    print("Clear")
    
docs()

print(docs.__doc__)      # print a function's docstring

print(max(10,20))

print(max.__doc__)