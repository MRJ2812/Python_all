get = int(input())
lst = []

for i in range(0,get):
    x,y = [int(x) for x in input().split()]
    
    try:
        sum = x/y
        lst.append(sum)
    except ZeroDivisionError:
        lst.append('divisao impossivel')
    

[print(x) for x in lst]
    
