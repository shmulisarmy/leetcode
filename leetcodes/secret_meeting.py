def chase(n):
    if n not in hash_set:
        return
    for i in hash_set[n]:
        if i in meeting_people:
            continue
        meeting_people.append(i)
        chase(i)


meetings = [[2,9,5], [1,2,5], [2,3,8], [1,5,10]]
first_person = 1


meeting_people = [1]
time_upto = 0
hash_set = {}


for m in meetings:
    if m[2] > time_upto:
        time_upto = m[2]
        hash_set = {}


    if m[0] in meeting_people:
        chase(m[1])
        meeting_people.append(m[1])
    else:
        if m[0] not in hash_set:
            hash_set[m[0]] = []
        hash_set[m[0]].append(m[1])
    if m[1] in meeting_people:
        chase(m[0])
        meeting_people.append(m[0])
    else:
        if m[1] not in hash_set:
            hash_set[m[1]] = []
        hash_set[m[1]].append(m[0])



print(meeting_people)