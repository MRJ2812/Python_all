if __name__ == '__main__':
    print("Enter how many proceess :",end="")
    n = int(input())
    
    avwt = 0; avtat = 0
    arrival = []
    burst= []
    completion = []
    tat = []

    for i in range(n):
        arrival.insert(i,int(input(f"Arrival time for p{i+1}: ")))           # Take arrival time.
        
    for i in range(n):
        burst.insert(i,int(input(f"Burst time for p{i+1}: ")))           # Take burst time.  
        
   
        
    for i in range(n):
        if i == 0:
            completion.insert(i,burst[i])
        else:
            completion.insert(i,completion[i-1]+burst[i])
    wt = [] 
    wt.insert(0,0)                   # First process waiting time is always 0
    
    for i in range(1,3):  
        wt.insert(i,completion[i-1]-arrival[i])    

    print("Processes  Burst Time  Waiting Time  Completion Time Turnaround Time")
    
    for i in range(3):
       tat.insert(i,burst[i]+wt[i])
       avwt+=wt[i]
       avtat+=tat[i]
       
       print(f"p{[i]}        {burst[i]}            {wt[i]}            {completion[i]}           {tat[i]}")
    print("hi  ",avtat) 
       
    avwt/=3
    avtat/=3
    
    print(f"Average waiting time{avwt}") 
    print(f"Average turnaround time {avtat}") 
 