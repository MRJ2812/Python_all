print("Enter Main Amount: ",end='')
main = int(input())
print("Enter compensative balance: ",end='')
compensative = int(input())
print("Enter interset: ",end='')
interset = int(input())
print("Enter period: ",end='')
time = int(input())
print("After tax: ",end='')
tax = int(input())


interest_sum = main * (interset/100) * (time/360)

compensative_sum = main * (compensative/100)

get = main - (compensative_sum+interest_sum)

EIR = (interest_sum/get) * (360/time) * 100

After_tex = (EIR/100) *(1-(tax/100)) * 100


print(f"{After_tex:.2f}%")