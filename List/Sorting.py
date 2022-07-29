list1 = [10,20,30,40,50,60]

# Two way to reverse
print(sorted(list1, reverse=True))          # This not actually change list1.



list1.sort(reverse = True)
print(list1)


# Use key in sort

list2 = ['Joy1','Joy3','Joy2']     

def second(list2):                   # Take list element everytime and return last value.
    return list2[-1]

list2.sort(key=second)                # We call the second function and get a return value,, and sort depend on this return value

print(list2)
