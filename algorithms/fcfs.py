from utils import print_gantt, print_results


def fcfs(processes):

    processes.sort(key=lambda x: x.arrival_time)

    time = 0
    gantt = []

    for p in processes:

        if time < p.arrival_time:
            time = p.arrival_time

        p.start_time = time

        time += p.burst_time

        p.finish_time = time

        gantt.append(p.pid)

    print("\n--- FCFS ---")

    print_gantt(gantt)

    print_results(processes)