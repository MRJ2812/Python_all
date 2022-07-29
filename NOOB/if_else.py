#Shorthand
x = 10
y = 20

if x == 10: print("This is short hand")


# == and != short hand
name = "joy"

if name is "joy":
    print("ok")
elif name is not "joy":
    print("no")


# Chaining
if 10 <= x <= 20:
    print("chaining")
     


# One line
print("First") if y == 15 else print("second")


# Another way of one line
print(x if x<y else y)

get = x if x>y else y


 
# Second else work like divide the code two part 
# Second print work on second 'if' condition 

print("if") if y > 10 else print("I am for this if->") if y == 20 else print("else")




#    if a is empty == not a
a = ""

if not a:
    print("empty") 
    
    
