import heapq
from utils import print_gantt, print_results

def priority_sched(processes):

    time = 0
    heap = []
    gantt = []
    incoming = processes[:]

    while incoming or heap:

        for p in incoming[:]:
            if p.arrival == time:
                heapq.heappush(heap, (p.priority, p))
                incoming.remove(p)

        if heap:

            _, p = heapq.heappop(heap)

            if p.start is None:
                p.start = time

            start = time
            p.remaining -= 1
            time += 1

            gantt.append((p.pid, start, time))

            if p.remaining == 0:
                p.finish = time
            else:
                heapq.heappush(heap, (p.priority, p))

        else:
            time += 1

    print("\n--- Priority Scheduling ---")
    print_gantt(gantt)
    print_results(processes)