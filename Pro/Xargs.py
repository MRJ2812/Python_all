# It's like rest and spread
# get's perameter like 'tuple' 


def xargs(*all):
    print(all)
    
xargs(10,20)

#--------------------------------


def xargs2(*num):
    sum = 0
    for get in num:
        sum += get
    print(sum)
    
xargs2(10,20,30)