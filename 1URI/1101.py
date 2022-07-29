lst = []
seq = ""
sum = 0
while True:
     x,y = [int(x) for x in input().split()]
     
     if x == 0 or y == 0:
         break
     
     else:
         for i in range(min(x,y),max(x,y)+1):
             seq += str(i) + " "
             sum += i
         
             enter = F"{seq}Sum={str(sum)}" 
             
             
         lst.append(enter)
         seq = ""
         sum = 0
                                   

for i in lst:
    print(i)