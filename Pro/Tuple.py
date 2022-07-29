# tuple is like list
# But not changeable (immutable)
# Tuple is faster than list
# !!! WE can keep tuple into tuple !!!


a = (10,-10,'joy',20.12)
another = 30,-20,"new"           # this is also a tuple

print(a)
print(a[2])
print(a[-1])

#length
print(len(a))

# Slicing like list
print(a[1:])


#Also use tuple like this
tuple1 =  ([1],2,3,4,5)

tuple1[0].append(5)

print(tuple1)

