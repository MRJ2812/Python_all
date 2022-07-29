# like list (unorderd)
# can't access value by index 
# Use for loop for show value
#   **  Don't support duplicate vlaue **

# *** For more info ,, check w3school --> set --> join set  


set1 = {1,2,3,4,"joy"}
set2 = set([15,25,35])

# Print set
print(set1)
# Add remove ,, len

set1.add(10)
set1.remove(3)
set2.discard(35)
print(len(set1))


# Another add value ,, Also if second one is tuple or list.
set1.update(set2)


# Check value
print(1 in set1)

print(2 not in set1)

###############################

print(set1 | set2)                  # union 

print(set1 & set2)                  # intesectoin
set1.intersection_update(set2)

print(set1 - set2)                  # Only keep unique of 'set1'. Whom are common with set2 and whom are not in set1 will delete. 


# Max min item
print(max(set1))
print(min(set1))