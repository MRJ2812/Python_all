def Present_value():
        print("Future value :" , end=" ")
        fv = int(input())
        print("Interest :",end=" " )
        i = int(input())
        print("How many Year  :",end=" " )
        n = int(input())
        print("Period in a Year (Not Zero) :",end=" " )
        m = int(input())
        
        sum = fv / pow( (1+((i/100)/m)),n*m)

        print(f"Normal Present Value {sum:0.2f} ")
        menu()
        
def Ordinary_Annuity():
        print("Future value :" , end=" ")
        fv = float(input())
        print("Interest  :",end=" " )
        i = float(input())
        print("How many Year  :",end=" " )
        n = float(input())
        print("Period in a Year (Not Zero) :",end=" " )
        m = float(input())
        
        sum = (fv * ( (1- (1/pow(1+((i/100)/m),n) )) / ((i/100)/m) ) )

        print(f"Ordinary Anunuity Present Value {sum:0.2f} ")
        menu()
        
def Due_Annuity():
        print("Future value :" , end=" ")
        fv = int(input())
        print("Interest  :",end=" " )
        i = int(input())
        print("How many Year  :",end=" " )
        n = int(input())
        print("Period in a Year (Not Zero):",end=" " )
        m = int(input())
        
        sum = (fv * ( (1- (1/pow(1+(i/100),n) )) / (i/100) ) ) * ((i/100) + 1)

        print(f"Due Anunuity Present Value {sum:0.2f} ")
        menu()

def fv_by_pv_ordinary():
        print("Present value :" , end=" ")
        pv = float(input())
        print("Interest  :",end=" " )
        i = float(input())
        print("How many Year  :",end=" " )
        n = float(input())
        print("Period in a Year (Not Zero):",end=" " )
        m = float(input())

        fv = pv / ( (1- (1/pow(1+((i/100)/m),n*m) )) / ((i/100)/m) )

        print(f"{fv:0.2f} ")
        menu()

        
def menu():
        print("\n1: Present value.")
        print("2: Present value with ordinary Annuity")
        print("3: Present value with due Annuity")
        print("4: Installment  (ordinary Annuity)")

        get = int(input())
        if get == 1:
            Present_value()
        elif get == 2:
            Ordinary_Annuity()
        elif get == 3:
            Due_Annuity()  
        elif get == 4:
            fv_by_pv_ordinary() 
         
menu()
    
