get = int(input())

lst = []
sum = 0
for i in range(0,get):
    X,Y = [int(x) for x in input().split()]
    
    for i in range(min(X,Y)+1,max(X,Y)):
         if i%2 != 0:
            sum += i
    
    lst.append(sum)
    sum = 0
 
 
    
for i in lst:
    print(i)