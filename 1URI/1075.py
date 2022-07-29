get_list = []

for i in range(0,5):
    get_list.append(int(input()))
    
    
maximum = max(get_list)

print(get_list.index(maximum)+1)



