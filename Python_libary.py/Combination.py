# It's like 1 2 3 , 2 1 3 

from itertools import combinations

list1 = [10,20,30,40,50]

list2 = list(combinations(list1,2))    # 2 means combination range ,, this library returns a list

print(list2)

#---------------------------------------------
# this is for original combinations .. first loop for index then loop for combination on those index range

list1 = [10,20,30,40,50]

for i in range(len(list1)+1):
    [print(list(x)) for x in combinations(list1,i)]    # it's nothing but devide the list and print it





