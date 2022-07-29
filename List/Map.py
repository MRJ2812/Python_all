# Comprehensions are easy than map
# Use for list 
# send list element to function one by one
# make list element change 

def add(list1):
    return(list1 * list1)
 
list1 = [10,20,30]  
    
get = list(map(add,list1))                                   #return as list
# or get = list(map(lambda x: x*x, list1))


print(get)


#-----------------------------
# this doesn't work

""" def add(list1):
    print(list1 * list1)
 
list1 = [10,20,30]  

add(list) """