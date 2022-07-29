""" yield is work like 'return' that retun value but don't break scope 
    we can get value if we want second time""" 
""" Second time it's give updated value but we should give another yield"""
# this is like range 


def show(x):
    while(x<=10):
        yield x
        x += 1
    
for i in show(2):
    print(i)

    






""" Documentation: Yield is like return ,, normally it return value but speciality is it can return
    upadated value (if we update any way) without break the scope of function.
    But for we should return new yield every time
    And also use 'new()' for print yield return value. 
"""