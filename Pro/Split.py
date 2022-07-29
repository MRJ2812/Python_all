#Split can devide num which are gave in one line  
# It's make list ,, don't break it

n = input()
list = n.split()

sum = 0

for x in list:
    sum = sum + int (x)

print(sum)



# It makes sigle string from list and list from sigle string
""" print("Joy,Hoy,Noy".split(",")) """