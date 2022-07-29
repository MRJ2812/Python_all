choose,amount = [int(x) for x in input().split()] 

sum = 0

if choose == 1:
     sum = 4 * amount
     
if choose == 2:
     sum = 4.5 * amount
     
if choose == 3:
     sum = 5 *  amount
     
if choose == 4:
     sum = 2 *  amount
     
if choose == 5:
     sum = 1.5 * amount


print("Total: R$ %.2f" % sum)