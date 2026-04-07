# Arrival Time-: It is the time at which a process enters the ready queue and becomes ready to execute on the CPU.It is the time when the process appears in the system.
# Burst Time-: It is the total amount of CPU time required by a process to complete execution.
# Waiting Time-: It is the total time a process spends waiting in the ready queue before getting CPU execution.
# Turnaround Time-: It is the total time taken from when a process arrives in the system until it completes execution.
# Turnaround Time = Waiting Time + Burst Time

from fcfs import fcfs
from processDataStructure import Process
from roundRobin import round_robin

def main():

    n = int(input("Enter number of processes: "))

    processes = []

    for i in range(n):

        pid = "P" + str(i+1)
        arrival = int(input(f"Arrival time of {pid}: "))
        burst = int(input(f"Burst time of {pid}: "))
        processes.append(Process(pid, arrival, burst))

    print("\nChoose Scheduling Algorithm")
    print("1. FCFS")
    print("2. Round Robin")
    print("3. SJF")
    print("4. Priority")

    choice = int(input("Enter choice: "))

    if choice == 1:
        fcfs(processes)

    elif choice == 2:
        q = int(input("Enter Time Quantum: "))
        round_robin(processes, q)

    elif choice==3:
        sjf(processes)
    
    elif choice==4:
        priority(processes)
    
    else:
        print("Enter a valid choice.")


main()