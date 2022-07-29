def with_same_interset():

        print("Enter Main Amount")
        main = int(input())
        print("Enter compensative balance")
        compensative = int(input())
        print("Enter interset")
        interset = int(input())

        interest_sum = main * (interset/100)
        compensative_sum = main * (compensative/100)

        get = main - (compensative_sum+interest_sum)

        EIRS = (interest_sum/get) * 100

        print(f"{EIRS:.2f}")
        
def collect_basis():
    
        print("Enter Main Amount")
        main = int(input())
        print("Enter compensative balance")
        compensative = int(input())
        print("Enter interset")
        interset = int(input())

        interest_sum = main * (interset/100)
        compensative_sum = main * (compensative/100)

        get = main - compensative_sum

        EIRS = (interest_sum/get) * 100

        print(f"{EIRS:.2f}")


def with_different_interest():
    
        print("Enter Main Amount")
        main = int(input())
        print("Enter usable balance %")
        usable = int(input())
        print("Interset for usable fund:")
        interset1 = int(input())
        print("Interest for unusable fund")
        interset2 = int(input())

        usable_fund = main * (usable/100)
        unusable_fund = main - usable_fund
        Interset_usable = usable_fund * (interset1/100)
        Interset_unusable = unusable_fund * (interset2/100)

        EIR = ((Interset_usable + Interset_unusable) / usable_fund) * 100



        print(f"{EIR:.2f}")
    


print("\n1 if same interest for full fund(discount basis)")
print("2 if same interest for full fund(collect basis)")
print("3 if different interest for  fund")



get = int(input())

if get == 1:
     with_same_interset()
elif get == 2:
     collect_basis()
elif get == 3:
     with_different_interest()

