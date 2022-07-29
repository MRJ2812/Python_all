list1 = [int(i) for i in input().split()]

lowest = sorted(list1)
highest = sorted(list1, reverse=True)

if lowest[0] == 0:
    lowest[0],lowest[1] = lowest[1],lowest[0]


high = ''
for i in highest:
    high += str(i)
    
low = ''
for i in lowest:
    low += str(i)

       
print(int(high)-int(low))