x,y = [int(x) for x in input().split()]


if x < y:
   for i in range(x,y+1):
      if i%2 != 0:
        print(i)
        
elif x > y:
   for i in range(x,y,-1):
      if i%2 != 0:
        print(i)
        


    


       
    