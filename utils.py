def print_gantt(gantt):

    print("\nGantt Chart:")

    for p in gantt:
        print(f"| {p} ", end="")

    print("|")


def print_results(processes):

    print("\nPID\tAT\tBT\tCT\tTAT\tWT")

    total_wt = 0
    total_tat = 0

    for p in processes:

        tat = p.finish_time - p.arrival_time
        wt = tat - p.burst_time

        total_wt += wt
        total_tat += tat

        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.finish_time}\t{tat}\t{wt}")

    n = len(processes)

    print("\nAverage Waiting Time:", round(total_wt/n,2))
    print("Average Turnaround Time:", round(total_tat/n,2))