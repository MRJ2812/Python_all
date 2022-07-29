print("Enter cash_discount: ")
cash_discount = int(input())
print("Enter actual_period : ")
actual_period= int(input())
print("Enter discount_period : ")
discount_period = int(input())


sum = (cash_discount/(100-cash_discount))  * (365/(actual_period-discount_period))

# sum = cash_discount / (100-cash_discount)

print((sum*100))