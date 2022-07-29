# From two list it take one element from each and concatinate them...
# keep them in tuple and all tuple's keep in a list

name = ['joy', 'muhhmmad', 'huraira']

roll = [10, 20, 30]

print(list(zip(name, roll)))               # As it return a list

# Also add item like

# 123 must string ,, integet not support
print(list(zip(name, roll, '123')))
