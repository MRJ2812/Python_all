Process_num = int(input("Enter total process number : ")) 
resource_num = int(input("Enter total resource number : ")) 

print("Enter allocation matrix ") 
allocation = [[int(i) for i in input().split()]for j in range(Process_num)]   # List comprehension
print("Enter Max_need matrix ") 
max = [[int(i) for i in input().split()]for j in range(Process_num)] 
print("Enter available matrix ") 
available = [int(i) for i in input().split()] 

need = [[0 for i in range(resource_num)] for j in range(Process_num)]     # Declare 2D empty array 

# Summation between maximum and allocation 
for i in range(Process_num): 
    for j in range(resource_num): 
        need[i][j] = max[i][j] - allocation[i][j] 
        
process = []                                                # Empty list

for x in range(Process_num):                                # 2 loop (process x process)
    if len(process) == Process_num:                         # if list length == to total process, break.
        break 
    for r in range(Process_num):                            #if process already in list, continue.
        if r in process: 
            continue 
        for c in range(resource_num):                      # if need > available , break
            if (available[c] < need[r][c]): 
                break 
        else: 
            for col in range(resource_num): 
                available[col] = available[col] + allocation[r][col] 
            process.append(r)                                          # enter process in list, after loop break.
        
print(process)