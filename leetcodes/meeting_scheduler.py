def minus_time(t1, t2):
    t1_hours = int(t1.split(':')[0]) * 60
    t1_mintues = int(t1.split(':')[1])
    t1_total_time = t1_hours+ t1_mintues

    t2_hours = int(t2.split(':')[0]) * 60
    t2_mintues = int(t2.split(':')[1])
    t2_total_time = t2_hours + t2_mintues

    print(f'{t1_total_time} - {t2_total_time} = {t1_total_time - t2_total_time}')

    return t1_total_time - t2_total_time


meeting_time = 30

p1_times = [['10:30', '11:40'], ['12:00', '12:30']]
p2_times = [['10:00', '11:00'], ['14:00', '12:30']]

p1_start_bound = ['9:00']
p2_start_bound = ['9:30']

p1_end_bound = ['16:00']
p2_end_bound = ['15:30']

start_bound = max(p1_start_bound, p2_start_bound)
end_bound = min(p1_end_bound, p2_end_bound)

all_times = []
all_times.extend(p1_times)
all_times.extend(p2_times)
all_times.extend([start_bound, end_bound])

#sorts list by meeting start time
all_times.sort(key= lambda x: int(x[0].replace(':', '')))
#outputs ['9:30'], ['10:00', '11:00'], ['10:30', '11:30'], ['12:00', '12:30'], ['14:00', '12:30'], ['15:30']
 
availible_meeting_times = []
pointer = 0
while pointer < len(all_times)-1:
    if minus_time(all_times[pointer + 1][0], all_times[pointer][-1]) >= meeting_time:
        availible_meeting_times.append([all_times[pointer][-1], all_times[pointer + 1][0]])
        pointer += 1
    else:
        all_times[pointer] = [all_times[pointer][0], max(all_times[pointer][1], all_times[pointer + 1][1])]
        all_times.pop(pointer + 1)

print(f'{availible_meeting_times = }')
