get = float(input())

new_salary = 0
Money_earned = 0
percentage = ""

if  get <= 400.0:
    new_salary = get + (get*(15/100))
    Money_earned = get*(15/100)
    percentage = "15 %"
   
elif  400<get<=800:
    new_salary = get + (get*(12/100))
    Money_earned = get*(12/100)
    percentage = "12 %"

elif  800<get<=1200:
    new_salary = get + (get*(10/100))
    Money_earned = get*(10/100)
    percentage = "10 %"

elif  1200<get<=2000:
    new_salary = get + (get*(7/100))
    Money_earned = get*(7/100)
    percentage = "7 %"

elif get > 2000:
    new_salary = get + (get*(4/100))
    Money_earned = get*(4/100)
    percentage = "4 %"
    
print(f"""Novo salario: {new_salary:0.2f} 
Reajuste ganho: {Money_earned:0.2f}
Em percentual: {percentage} """)