# Function to find the waiting time  for all processes  
def findWaitingTime(processes, n, wt): #wt-waiting time, n-no. of processes   
    burst = [0] * n                                # Copy the burst time into rt[]  
  
    # Copy the burst time into rt[]  
    for i in range(n):  
        burst[i] = processes[i][1] 
    complete = 0
    running_time = 0
    minm = 999999999
    short = 0
    check = False
  
    # Process until all processes gets  
    # completed  
    while (complete != n): 
          
    # Find process with minimum remaining time
    # among the processes that arrives till the current time.
        for j in range(n): 
            if ((processes[j][2] <= running_time) and (burst[j] < minm) and burst[j] > 0):         # arrival time <= running time(0) || burst time < 9999 || burst > 0
                minm = burst[j]                                          # minm = running burst time (5)
                short = j                                                      # sort = process  (1)
                check = True
        if (check == False): 
            running_time += 1                                               # if no process come this time, increase running time.
            continue
              
        # Reduce burst time of running process by one  (4)
        burst[short] -= 1
  
        # Update minimum  
        minm = burst[short]                        # minm = running process burst time.
        if (minm == 0):                            # if burst time 0 then make it infinity like before
            minm = 999999999
  
        # If a process gets completely executed  
        if (burst[short] == 0):  
  
            # Increment complete  
            complete += 1                               # Complete 1 process
            check = False
  
            # Find finish time of current process  
            fint = running_time + 1
  
            # Calculate waiting time  
            wt[short] = (fint - proc[short][1] - proc[short][2]) 
  
            if (wt[short] < 0): 
                wt[short ] = 0
          
        # Increment time  
        running_time += 1
  
# Function to calculate turn around time  
def findTurnAroundTime(processes, n, wt, tat):  
      
    # Calculating turnaround time  
    for i in range(n): 
        tat[i] = processes[i][1] + wt[i]  
  
# Function to calculate average waiting  and turn-around times.  
def findavgTime(processes, n):  
    wt = [0] * n 
    tat = [0] * n  
   
    findWaitingTime(processes, n, wt)  
   
    findTurnAroundTime(processes, n, wt, tat)  
  
    # Display processes along with all details  
    print("Processes    Burst Time     WaitingTime     Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", processes[i][0], " ",  processes[i][1], " ",  wt[i], " ", tat[i]) 
  
    print("Average waiting time = %.5f "%(total_wt /n) ) 
    print("Average turn around time = ", total_tat / n)  
      
  
if __name__ =="__main__": 
      
    # Process id's  
    proc = [[1, 5, 0], [2, 3, 1],                     # second one is burst time
            [3, 4, 2], [4, 1, 4]] 
    n = 4
    findavgTime(proc, n) 
