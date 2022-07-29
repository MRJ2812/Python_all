# if we  give exception without type...finally print whatever happend.
# Finally work when exception don't match with excepiton type
# Finally print it's code but can't handle exception



try:
    print(20/'joy')
except:
    print("ok")
finally:
    print("I will print whatever happend")


#_____________________________________________________________

try:
   sum = 20 / 0
   print(sum)
   
except ZeroDivisionError:
    print("Sorry")  

finally:
    print("If exception can't handle then finally work")
    


