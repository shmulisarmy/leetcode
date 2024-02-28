class Meeting():
    def __init__(self, start_time, end_time, cost):
        self.start_time = start_time
        self.end_time = end_time
        self.cost = cost


    @staticmethod
    def find_best_time_to_place_meeting(target: int, meetings: ["Meeting"]) -> int:
        p1: int = 0
        p2: int = 0
        cost_so_far = meetings[0].cost
        best_cost_so_far = float('inf')

        while True:
            if meetings[p2].start_time - meetings[p1].end_time < target:
                cost_so_far += meetings[p2].cost
                p2 += 1
                if p2 == len(meetings):
                    break
            else:
                if cost_so_far < best_cost_so_far:
                    best_cost_so_far = cost_so_far
                    new_meeting_time = f"{meetings[p1].end_time} - {meetings[p2].start_time}"
                p1 += 1
                cost_so_far -=  meetings[p1].cost


        print(new_meeting_time or False, best_cost_so_far)

meetings = [Meeting(0, 0, 0), Meeting(1, 3, 2), Meeting(5, 12, 4), Meeting(8, 11, 5), Meeting(13, 16, 0)]
for target in range(9):
    Meeting.find_best_time_to_place_meeting(target, meetings)