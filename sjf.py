#SJF selects the process that has the smallest burst time among all processes that have arrived.

from utils import print_gantt, print_results

def sjf(processes):

    time = 0
    gantt = []
    remaining = processes[:]
    completed = []

    while remaining:

        available = [p for p in remaining if p.arrival <= time]

        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x.burst)

        remaining.remove(p)

        p.start = time
        time += p.burst
        p.finish = time

        gantt.append((p.pid, p.start, p.finish))

        completed.append(p)

    print("\n--- SJF ---")
    print_gantt(gantt)
    print_results(completed)