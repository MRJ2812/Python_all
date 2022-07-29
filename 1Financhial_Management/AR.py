def AR():
    print("\n\nIf AR time per month input 12\n")
    print("Enter Company AR")
    AR = int(input())
    print("interest for AR")
    interset = int(input())
    print("time for AR")
    time = int(input())
    print("Average Collection period")
    collection_time = int(input())
    
    
    AR = (AR*time*collection_time) / 360
    ART = 360 / collection_time
    
    factor_comission = AR * (2 / 100)
    reserve = AR * (20/100)
    interest = (AR - factor_comission - reserve) * (12/100) * (collection_time/360)
    
    final_loan = (AR - factor_comission - reserve - interest)
    print(f"{final_loan:.2f} ")
    
    
AR()