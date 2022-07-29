# This is like object but we can't keep 'key' value as noraml variable name....
# Should declare as string
# WE can keep dictionaries into dictionaries 

dic = {
    "101" :"JOY",
    "102":"himu",
    10 : 123
}

# Add value
dic["new"] = 100

#Another way
dic.update({"life":"nothing"})

print(dic)
print(dic.items())

#Delete value
del dic['new']


# Get values
print(dic["101"])                       

print(dic.get("102"))                   

# if key is not exist
print(dic.get("104","no value"))          


# print all keys
print(dic.keys())
##                get = list(dic.keys())

# print all values
print(dic.values())
##                get = list(dic.values())


#copy dictionary
copy = dic.copy()


# -------------------------------------------------

# If We have two keys as same name,, as dictionary not support duplicate 

classroom = {'Boys':{'Messi':{'Match':100,'Win':90,'Goal':80},
                    'Ronaldo':[{'Match':100,'Win':80,'Goal':70},{'Match':50,'Win':30,'Goal':40}] }         
            }

print(classroom['Boys']['Ronaldo'][1]['Match'])


