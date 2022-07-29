# myfunc(2) argument go to 'myfunc' function return a lambda with a value of n=2
# those lambda stored in  mydoubler and mydoubler now work like a lambda with a value of n=2

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))              # imagine mydoubler() as a lambda()
print(mytripler(11))