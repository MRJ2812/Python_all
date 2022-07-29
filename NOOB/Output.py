# Digit after decimal 1
a = 10

print(f" hi {a : 0.2f}")

# other way
sum  = 10.0000 
print("Total : %.2f" % sum)


# another way
# But it return string
print("total :",format(sum,".3f"))

# Fomatting
num1 = 10
num2 = 20

print(f"hi {num1} + {num2} = {num1+num2}")


# Cut new line in two print
print("hi this is ine line",end=" ")
print("yap")
