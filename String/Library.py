# Get string as word
name = 'My name is joy'
for i in name.split():
    print(i)


## Find string index by element
## It return the first 'p' of 'poor'. it check the hole world  !!!
## Give the first poor 

string = 'Thep lyrics is not that poor The lyrics is poor'
print(string.index('poor'))
print(string.find('poor'))       # Another way


### Revarse a string
name = 'madam'

for i in reversed(name):
    print(i)


# Consider as a  list breaker 
print(",".join(["My",'name','is','joy']))


# all split are same ,,  oposite join function
# It makes sigle string from list and list from sigle string
print("M,R,joy".split(","))

# String replacer
print("Hellow Joy".replace('Joy', 'noone'))

# Checker "Start with"
print("hi my name is joy".startswith('hi'))

# Checker "end with"
print("hi my name is joy".endswith('joy'))


### Make first word capital
string2 = 'my name'
print( string2.title() )

# Upper Lower
print("hi hello".upper())
print("HI HELLOW".lower())



# Delete space
name = 'Rahman \n '

print(name)

print(name.rstrip())