list1 = [1,2,3,4]

# print one by one
[print(x) for x in list1]


# for loop get the list and first 'x' means print or return answer .. also called 'Expression'
get = [x for x in list1]

print(get)

#-----------------------------------------------------------------

get2 = [x*x for x in list1]

print(get2)


#------------------------------------------------------------------

# With a condition 
get3 = [x for x in list1 if x % 2 == 0]

print(get3) 