try:
   sum = 20 / 0
   print(sum)
   
except:
    print("Sorry")
    
    
#-------------------------------------------------

# We can also use error quality

try:
   sum = 20 / 0
   print(sum)
   
except (ValueError,ZeroDivisionError):
    print("Sorry")
    exit()              # -----------> if error ocurs , it will stop the programm.      
    
    
# If we don't know the type of exception and want to know that

try:
   sum = 20 / 0
   print(sum)
   
except Exception as e:
    print(e)