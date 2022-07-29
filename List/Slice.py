list1 = [10,20,30,40]


# travel list
print(list1[1:])
print(list1[:3])
print(list1[1:3])                # only 20 and 30
print(list1[-3:-1])              # tips :- can't run from 40 to 20
print(list1[-3:])                # travarse to last element



print("After 2 index----",list1[0:4:2])


list1[1:2] = ['This','New']         # It eat only num 2 index and filled with 'this','new'
print("[1:2]--",list1)

list1[1:4] = ['This','New']         # It eat num 1 to 3 index and filled with this new

print("[1:4]--",list1)


print("\n\n")

# This two are not same

list2 = [1,2,3,4]

list2[2] = ["Yu",'Dj']
print(list2)


list2[1:2] = ["Add","two"]
print(list2)