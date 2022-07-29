# We can give error masage in if else condition

def check(age):
    
    if age < 18:
        raise ValueError("You litte man")
    
    return print("You are allowed")    


check(14)



#---------------------------------------------------------
# we can also keep this in try except

#try:
 #   check(15)
#except:
 #   print("Ok we delete 'Value error'")