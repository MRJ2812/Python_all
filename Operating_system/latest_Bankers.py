from concurrent.futures import process
from zoneinfo import available_timezones


print("Enter how many process")
p = int(input())
print("Enter how many resource")
r = int(input())

print("Enter allocation matrix")
allocation = [[int(i) for i in input().split()]for j in range(p)]   # input().split

print("Enter maximum matrix")
max = [[int(i) for i in input().split()]for j in range(p)]   # int(i)

print("Input available matrix")
avilable = [int(i) for i in input().split()]

need = [[0 for i in range(r)] for j in range(p)]            # O in

for i in range(p):
    for j in range(r):
        need[i][j] = max[i][j] - allocation[i][j]
    
process = []    
        
for x in range(p):
    for row in range(p):
        if row in process:
            continue
        for col in range(r):
            if (avilable[col] < need[row][col]):
                break
        else:
            for col in range(r):
                avilable[col] += need[row][col]
            process.append(row)
                 

print(process)  