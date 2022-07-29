def with_brokerage():
    print("Enter Face value")
    face = int(input())
    print("Enter Selling value")
    sell = int(input())
    print("Brokerage fee")
    brokerage = int(input())
    print("Enter Time value")
    time = int(input())

    EIR = (((face-sell)/(sell-brokerage)) * (365/time)) * 100

    print(f"\n{EIR:.2f}")
    
def without_brokerage():
    print("Enter Face value")
    face = int(input())
    print("Enter Selling value")
    sell = int(input())
    print("Enter Time value")
    time = int(input())

    EIR = (((face-sell)/sell) * (365/time)) * 100

    print(f"\n{EIR:.2f}")
    
print("1.with_brokerage\n2.without_brokerage")
get = int(input())

if get == 1:
    with_brokerage()
if get == 2:
    without_brokerage()
    
