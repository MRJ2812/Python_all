def display(x,y):
    yield x
    yield y
  
  
m,n = display(10, 20)             # Take same num of variable         
print(m,n)


# another way to display . Next get every  value sequently . First take value in another  variable

get = display(100, 200)
print(next(get)) 
print(next(get)) 

