# from processDataStructure import Process
# from fcfs import fcfs
# from sjf import sjf
# from roundRobin import round_robin
# from priority import priority_sched


# def create_processes():

#     return [
#         Process("P1",0,8,3),
#         Process("P2",1,4,1),
#         Process("P3",2,2,4),
#         Process("P4",3,5,2)
#     ]


# def main():

#     fcfs(create_processes())
#     sjf(create_processes())
#     round_robin(create_processes(),3)
#     priority_sched(create_processes())


# # if __name__ == "__main__":
# #     main()

# main()


from process import Process
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.round_robin import round_robin
from algorithms.priority_sched import priority_sched


def create_processes():

    processes = []

    n = int(input("Enter number of processes: "))

    for i in range(n):

        pid = f"P{i+1}"

        arrival = int(input(f"{pid} Arrival Time: "))
        burst = int(input(f"{pid} Burst Time: "))
        priority = int(input(f"{pid} Priority: "))

        processes.append(Process(pid, arrival, burst, priority))

    return processes


def main():

    processes = create_processes()

    fcfs([Process(p.pid,p.arrival_time,p.burst_time,p.priority) for p in processes])

    sjf([Process(p.pid,p.arrival_time,p.burst_time,p.priority) for p in processes])

    round_robin([Process(p.pid,p.arrival_time,p.burst_time,p.priority) for p in processes],3)

    priority_sched([Process(p.pid,p.arrival_time,p.burst_time,p.priority) for p in processes])


if __name__ == "__main__":
    main()