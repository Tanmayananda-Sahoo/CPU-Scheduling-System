# from utils import print_gantt, print_results

# def sjf(processes):

#     time = 0
#     gantt = []
#     remaining = processes[:]
#     completed = []

#     while remaining:

#         available = [p for p in remaining if p.arrival <= time]

#         if not available:
#             time += 1
#             continue

#         p = min(available, key=lambda x: x.burst)

#         remaining.remove(p)

#         p.start = time
#         time += p.burst
#         p.finish = time

#         gantt.append((p.pid, p.start, p.finish))

#         completed.append(p)

#     print("\n--- SJF ---")
#     print_gantt(gantt)
#     print_results(completed)


from utils import print_gantt, print_results


def sjf(processes):

    time = 0
    remaining = processes[:]
    completed = []
    gantt = []

    while remaining:

        available = [p for p in remaining if p.arrival_time <= time]

        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x.burst_time)

        remaining.remove(p)

        p.start_time = time

        time += p.burst_time

        p.finish_time = time

        gantt.append(p.pid)

        completed.append(p)

    print("\n--- SJF ---")

    print_gantt(gantt)

    print_results(completed)