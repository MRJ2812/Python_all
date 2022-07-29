# If we have Future value and paresent value...and interest rate
# We can find year time

import math

while True:
        

        print("\nFuture value :",end=" " )
        fv = float(input())
        print("Present value :" , end=" ")
        pv = float(input())
        print("Interest value :",end=" " )
        i = float(input())
        print("Period in a Year :",end=" " )
        m = float(input())

        year = math.log(fv/pv) / (math.log(1+((i/100)/m)) * m) 

        print(year,"\n\n")
        