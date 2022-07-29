dic =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

list1 = []
for i in dic:
    list1.append(list(i.values()))

print(set(list1))