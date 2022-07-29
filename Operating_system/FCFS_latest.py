from pip import main
# def waiting_time(p,at,bt):



if __name__ == "__main__": 
    print("Enter how many process")
    p = int(input())


    at = [] 
    bt = [] 
    wt = [] 
    tat = [] 

    for i in range(p):
        print("Arrival time of process",i)
        at.append(int(input()))
        print("Burst time of process",i)
        bt.append(int(input()))    
 
    
    running_time = 0
    
    finish = 0
    
    for i in range(p):
        if at[i] == running_time:          
            finish = finish + bt[i] 

            wt.append(finish - at[i] - bt[i])
            tat.append(wt[i]+bt[i])
        
        running_time += 1
    
    print(wt)
    print(tat)