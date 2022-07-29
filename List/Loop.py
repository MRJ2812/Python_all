list = [10,20,30,40]

# Loop as index num
for x in range(len(list)):           # range(3)
    print(list[x])
    
    
# In while loop
i = 0
while i < len(list):
  print(list[i])
  i = i + 1
  
  
# Make a auto list
newlist = [x for x in range(10)]

print(newlist)  


# List in list and print item 
lst = [['joy',1], ['tawmid',2], ['risana',3]]

for i,item in lst:
    print(i,item)
    

# Find the string value
x = [2,4,6,10,15,13,'joy']


for i in x:
    if str(i).isnumeric():            # "isnumaric" only work on string variable
        print(i)

