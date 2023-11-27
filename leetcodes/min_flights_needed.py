def follow_flight_back_to_origin(flight, trail):
    if flight[0] not in landings:
        return True



flights = [
    (1, 3),
    (5, 4),
    (4, 5),
    (1, 2),
    (1, 6)
]

reqs = list(range(1, 7))
start_flight = 1


landings = {i[1]: i[0] for i in flights}

for i in reqs:
    if i not in landings:
        flights.append(start_flight, i)