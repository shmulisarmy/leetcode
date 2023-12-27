




points = [
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0]
]

found_pairs = []


for i in range(len(points)):
    for j in range(len(points[0])):
        if points[i][j]:
            for k in range(j + 1, len(points[0])):
                if points[i][k]:
                    for l in range(len(points)):