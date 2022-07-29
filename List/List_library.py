list1 = [1,2,"F",'F',3,4,5]
list2 = [1,2,3,4,5,6]

# here we can copy but if we change copy array the main array will change.
array=[10,20,30,40]
list1 = array



# Making auto list
list3 = list(range(5))
print(list3)


# find length
print(len(list1))            

# add value
list1.append(100)

# add in specific index ** It can't replace value ,, value will side right
list1.insert(0,"Hello")   

# Many append
get = list1 + ['N','e','w']

# Remove
list1.remove(2)
list1.remove('F')
list1.pop()                       # remove last element as default
list1.pop(1)

# Delete item
del(list1[3]) ; del(list1[4])
   

#Insert another list  in last position
list1.extend(list2)
print(list1)

# Find first occurance 
list1.index('F')


# Find max / min
print(max(list2))
print(min(list2))

# Count
list4 = [1,1,1,2,2]
print(list4.count(1))


# Reverse ,, it's reverse the main list
list2.reverse()
print(list2)


# sort desending the list 
get = sorted(list2,reverse=True)               ## This sorted return value one by one in a loop
for i in get:
    print(i)
    

list2.sort()
print(list2)
 ## This sorted return all value at a time in a loop



""" !!!
after reverse or sort we can't take them anothe vaiable 
list2.sort()
li = list2  """

#Sort as reverse
list2.sort(reverse = True)



# Copy a list
new = list2.copy()
print(new)

# this list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Sum all element of a list
print(sum(list2))


