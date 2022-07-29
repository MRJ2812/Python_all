# First import reduce
# reduce(function, list)  , Must give 2 value as argumant 
# it takes first 2 value and calculate them ,, then take result and calculate with third one




from functools import reduce

list1 = [10,20,30]

get = reduce(lambda x,y : x*y ,list1)
print(get)