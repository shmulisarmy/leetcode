import random

class TimeStamp:
    def __init__(self, time, start, cost):
        self.time = time
        self.start = start 
        self.cost = cost

    @staticmethod
    def create_stamps(start, end, cost):
        return TimeStamp(start, True, cost), TimeStamp(end, False, -cost)

times = [
    [1000, 1015],
    [1030, 1045],
    [1100, 1115],
    [1200, 1215],
    [1230, 1245],
    [1400, 1415],
    [1430, 1445],
    [1500, 1515],
    [1530, 1545],
    [1600, 1615]
]

new_times = [TimeStamp.create_stamps(start, end, random.randint(1, 10)) for start, end in times]

# Sort the new_times based on the time attribute of each TimeStamp object
new_times.sort(key=lambda x: x[0].time)


times = []
# Printing the sorted new_times
for stamp_pair in new_times:
    for stamp in stamp_pair:
        times.append(stamp)
        
for stamp in times:
    print(f"Time: {stamp.time}, {'Start' if stamp.start else 'End'}, Cost: {stamp.cost}")

def main(target_time):

	cost = p1 = p2 = 0
	min_cost = found_meeting_time = None

	while True:
		not_enough_meeting_time = times[p2].time < times[p1].time + target_time
		if not_enough_meeting_time or not times[p2].start:
			if times[p2].start:
				cost += times[p2].cost
			p2 += 1
			if p2 == len(times):
				break
		else:
			if not (min_cost and cost >= min_cost):
				min_cost = cost
				found_meeting_time = f"{times[p1].time}-{times[p2].time}"
			# see if we can get a lower cost by getting to the end and remove the cost from the meeting start
			p1 += 1
			if not times[p1].start:
				cost += times[p1].cost


	return f"{min_cost = }, {found_meeting_time = }"

print(main(60))