def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# First 2 go as myfunc perameter
# then mydoubler works as lambda perameter

#------------------------------

def myfunc2(n):
  return lambda a : a * n

mydoubler = myfunc2(2)
mytripler = myfunc2(3)

print(mydoubler(11))
print(mytripler(11))