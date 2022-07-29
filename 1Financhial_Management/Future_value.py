def future_value():
        print("Present value :" , end=" ")
        pv = int(input())
        print("Interest rate :",end=" " )
        i = int(input())
        print("How many Year  :",end=" " )
        n = int(input())
        print("Period in a Year :",end=" " )
        m = int(input())
        
        sum = pv * pow ( (1+( (i/100)/m )) , (n*m))

        print(f"Normal Future Value {sum:0.2f} ")
        menu()
        
def FV_ordinary():
        print("------------------ End  Of The Year ---------------------\n ")

        print("Present value :" , end=" ")
        pv = int(input())
        print("Interest value :",end=" " )
        i = int(input())
        print("How many Year  :",end=" " )
        n = int(input())
        print("Period in a Year :",end=" " )
        m = int(input())

        sum = pv * ((pow(1+((i/100)/m),n*m)-1)/((i/100)/m))

        print(f"{sum :.2f}")
        menu()
        
def FV_due():
        print("------------------ Start  Of The Year ---------------------\n ")

        print("Present value :" , end=" ")
        pv = int(input())
        print("Interest value :",end=" " )
        i = int(input())
        print("How many Year  :",end=" " )
        n = int(input())
        print("Period in a Year :",end=" " )
        m = int(input())

        sum = pv * (((pow(1+((i/100)/m),n*m)-1) / ((i/100)/m))  * (1+((i/100)/m)))

        print(f"{sum :.2f}")
        menu()

def pv_by_fv():
        print("Present value :" , end=" ")
        fv = int(input())
        print("Interest value :",end=" " )
        i = int(input())
        print("How many Year  :",end=" " )
        n = int(input())
        print("Period in a Year :",end=" " )
        m = int(input())

        pv =  fv /  (((pow(1+((i/100)/m),n*m)-1) / ((i/100)/m))  * (1+((i/100)/m))) 


        print(f"{pv : .2f}" )
        menu()


   
def menu():
    print("\n1: Normal Future value.")
    print("2: Future value with ordinary Annuity (End  Of The Year)")
    print("3: Future value with due Annuity  (Start  Of The Year)")
    print("4: Installment   (Due anuuity)" )
    get = int(input())
    if get == 1:
        future_value()
    elif get == 2:
        FV_ordinary()
    elif get == 3:
        FV_due()
    elif get == 4:
        pv_by_fv()


menu()
        
        