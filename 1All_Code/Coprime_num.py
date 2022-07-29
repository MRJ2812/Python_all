n = int(input())
m = int(input())

list1 = []
list2 = []

for i in range(2,n):
    if n % i == 0:
        list1.append(i)
        
for i in range(2,m):
    if m % i == 0:
        list2.append(i)
        
count = 0
for i in list1:
    for j in list2:
        if i == j:
            print("Not Comprime")
            count = 1
            break


if count == 0:
    print("Co prime")
        