def findWaitingTime(arrival,b, p, wt): 
    burst = [0] * p                            
   
    for i in range(p):                         
        burst[i] = b[i]
        
    complete = 0
    running_time = 0
    minm = 999999999
    rp = 0
    check = False  
    
    while (complete != p): 
          
        for j in range(p): 
            if ((arrival[j] <= running_time) and (burst[j] < minm) and burst[j] > 0):        
                minm = burst[j]  
                rp = j                                      
                check = True
                
        if (check == False): 
            running_time += 1                                               
            continue
                  
        burst[rp] -= 1
         
        minm = burst[rp]  
                               
        if (minm == 0):                           
            minm = 999999999
    
        if (burst[rp] == 0):  
            
            complete += 1                              
            check = False                       
               
            finish = running_time + 1 
  
 
            wt[rp] = (finish - b[rp] - arrival[rp])       
  
            if (wt[rp] < 0):                          
                wt[rp ] = 0
                    
        running_time += 1
  
 
def findTurnAroundTime(b, p, wt, tat):  
       
    for i in range(p): 
        tat[i] = b[i] + wt[i]  
  

def findavgTime(arrival,b, p):  
    wt = [0] * p 
    tat = [0] * p  
   
    findWaitingTime(arrival,b, p, wt)  

   
    findTurnAroundTime(b, p, wt, tat)  
   
    print("Processes    Burst Time     WaitingTime     Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    
    for i in range(p): 
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", i, "\t\t",  b[i], "\t\t",  wt[i], "\t\t", tat[i]) 
  
    print(f"Average waiting time = {total_wt /p} ") 
    print(f"Average turn around time =  = {total_tat /p}") 
 
      
  
if __name__ =="__main__": 
    
    print("Enter how many proceess :",end="")
    p = int(input())
    
    arrival = []
    b = []

    for i in range(p):
        arrival.insert(i,int(input(f"Arrival time for p{i+1}: ")))               
          
    for i in range(p):
        b.insert(i,int(input(f"Burst time for p{i+1}: ")))  
        
    findavgTime(arrival,b, p) 
      

