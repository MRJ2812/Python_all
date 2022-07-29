## 2D Array
array1 = []
for _ in range(0,int(input())):
    array1.append([input(), float(input())])
    
print(array1)

## Another 2D
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]


## First input one value , second input many at a line.

name, *marks = input().split()

print(name)
print(marks)