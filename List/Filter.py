# Comprehensions are easy than filter
# Use for list 
# send list element to function one by one
# make list element change 

list1 = [1,2,3,4]


# Check if the function condition match.. Whole lambda functoin is like a condition
# If condition match ,, it return true ,, filter strore the true condition value and we strore as a list
get = list(filter(lambda x : x%2 == 0, list1))

print(get)