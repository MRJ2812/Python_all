## This code is for get values from list

dic =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

list1 = []
for i in dic:
    print(list(i.values())[0])
    
    
## Check key in dictionary

# list length in dictionary

Sample_data = {'item1': [10,20,30]}

new = list(map(len,Sample_data.values()))

print(new)

