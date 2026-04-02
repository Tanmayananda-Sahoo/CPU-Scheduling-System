def fcfs(processes):
    processes.sort(key=lambda x: x.arrival)

    time=0
    total_wait=0
    total_turn=0
    print("\nGantt Chart:")

    for p in processes:
        p.arrival = p.arrival[0]
        p.waiting = p.waiting[0]
        p.burst = p.burst[0]

        if time < p.arrival:
            time = p.arrival
        p.waiting = time - p.arrival
        p.turnaround = p.waiting + p.burst

        time+= p.burst

        total_wait += p.waiting
        total_turn += p.turnaround

        print("|", p.pid[0], end=" ")
    print("|")
    print("\nProcess\tWaiting\tTurnaround")

    for p in processes:
        print(p.pid[0], "\t", p.waiting, "\t", p.turnaround)
    print("\nAverage Waiting Time: ", total_wait/len(processes))
    print("\nAverage Turnaround Time: ", total_turn/len(processes))