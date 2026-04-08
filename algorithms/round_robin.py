from collections import deque
from utils import print_gantt, print_results


def round_robin(processes, quantum):

    queue = deque()
    time = 0
    gantt = []

    incoming = processes[:]

    while incoming or queue:

        for p in incoming[:]:
            if p.arrival_time <= time:
                queue.append(p)
                incoming.remove(p)

        if not queue:
            time += 1
            continue

        p = queue.popleft()

        if p.start_time is None:
            p.start_time = time

        run_time = min(quantum, p.remaining_time)

        time += run_time

        p.remaining_time -= run_time

        gantt.append(p.pid)

        for pr in incoming[:]:
            if pr.arrival_time <= time:
                queue.append(pr)
                incoming.remove(pr)

        if p.remaining_time > 0:
            queue.append(p)
        else:
            p.finish_time = time

    print("\n--- Round Robin ---")

    print_gantt(gantt)

    print_results(processes)