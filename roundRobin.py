def round_robin(processes, quantum):

    time = 0
    queue = processes.copy()
    remaining = {p.pid: p.burst for p in processes}

    print("\nGantt Chart:")

    while queue:

        p = queue.pop(0)

        if remaining[p.pid] > quantum:

            print("|", p.pid, end=" ")

            time += quantum
            remaining[p.pid] -= quantum
            queue.append(p)

        else:

            print("|", p.pid, end=" ")

            time += remaining[p.pid]
            remaining[p.pid] = 0
    print("|")