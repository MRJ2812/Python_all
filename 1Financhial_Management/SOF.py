def payback():
    print("Enter investment: ",end='')
    nco = int(input())
    print("Enter Year :- whose cumulative nearest of investment: ",end='')
    A = int(input())
    print("Enter cumulative :- whose nearest of investment: ",end='')
    c = int(input())
    print("Next year cash flow (not cumulative): ",end='')
    d = int(input())
    
    payback = A + (nco-c)/d
    print(f"{payback:.2f}")
    

def Rate_of_return():
    print("\nTotal year: ",end='')
    year = int(input())
    
    total_cashInlow = 0
    print("Enter all cashinflow")
    for i in range(year):
       
        total_cashInlow += int(input())
        
    average_cashinflow = total_cashInlow / year
    
    print("Initial capital: ",end='')
    inithial = int(input())
    print("Additional capital: ",end='')
    additional = int(input())
    
    avg_capital = (inithial+additional) / 2
    
    
    ARR = (average_cashinflow/avg_capital) * 100
    
    print(f"{ARR:.2f}")
        

def NVP():
    print("Enter dicount rate: ")
    R = int(input()) / 100
    print("Enter investment: ")
    C = int(input())
    print("enter year")
    temp = int(input())
    
    print("Enter all cashflow: ")
    
    sum = 0
    j = 1
    for i in range(temp):
        sum += int(int(input())/ ((1+R)**j))
        j += 1
    
    print(f"sum ={sum-C}")


print("\n1.payback period")
print("2.Accounting Rate_of_return")
print("3.Net present value: ")

get = int(input())

if get == 1:
    payback()
elif get == 2:
    Rate_of_return()
elif get == 3:
    NVP()
    
    

    