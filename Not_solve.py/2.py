## Run this code ... how a tuple made

N = int(input())
cont = 0
a,b,c = 1,2,3
while cont < N:
    print('{10} {20} {30} PUM'.format(a,b,c))          # ?? Don't unterstand this
    c+=2
    a = c
    b = c
    b+=1
    c+=2
    cont+=1