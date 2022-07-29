# also called anonymus function
# no body

# right side first brace is argument
# auto return result


get = (lambda x,y : x+y )(10,20)

print(get)


#-----------------------------------------------------------

lam = lambda a : a+10

print(lam(5))

# One line condition
print((lambda x,y: x if x>y else y)(10,20))