# class Process:
#     def __init__(self, pid, arrival, burst, priority):
#         self.pid = pid,
#         self.arrival = int(arrival),
#         self.burst = burst,
#         self.waiting = 0,
#         self.turnaround = 0,
#         self.remaining = burst,
#         self.priority = priority,
#         self.start = None,
#         self.finish = None

class Process:

    def __init__(self, pid, arrival_time, burst_time, priority):

        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        self.remaining_time = burst_time

        self.start_time = None
        self.finish_time = None