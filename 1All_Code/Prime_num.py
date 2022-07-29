# It's a way to find prime ..........

get1 = int(input())
get2 = int(input())

# n = int((get1+1)/6)

# while True:
#     if (6*n-1)%5 != 0  and (6*n-1)%7 != 0:
#         print(6*n-1)
#     if (6*n+1)%5 != 0 and (6*n+1)%7 != 0:
#         print(6*n+1)
   
#     n += 1
#     if (6*n+1) >= get2:
#             break


for i in range(get1,get2+1):
    if i % 2 != 0:
        if i % 3 != 0 and  i % 5 != 0 and  i % 7 != 0 and  i % 9 != 0:
            print(i)

