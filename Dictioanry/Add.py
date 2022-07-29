a = {"name":500,
     "roll":463}

c = {"joy":500,
     "hellow":463}

new = {}

for i in (a,c):
    new.update(i)           # Update make all dictioanry in new one dictionary in one time.
print(new)