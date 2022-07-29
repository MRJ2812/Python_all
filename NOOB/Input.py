# Multiple 1
x,y,z = input().split()
a, b, c  = int (x), int(y),int(z)

print(a, b, c)


# Multiple 2
# whole right side part is a 'list' // we can also use tuple ()
l,n,m = [int(x) for x in input().split()] 

print(l, m, n)

# Take input for list in a single line
get = [int(i) for i in input().split()]


# Only one
get = [float(x) for x in input().split()]


# This is a fastest way to take and prit it.
print(name:=input())