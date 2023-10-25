def scout_island(row, col):
    looked_at.add((row, col))
    for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
        if -1 < i < rows and -1 < j < cols:
            if board[i][j] == 1 and (i, j) not in looked_at:
                scout_island(i, j)

board = [[0,0,1,1,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [1,0,0,0,1],
         [1,0,0,0,1],]

rows = len(board)
cols = len(board[0])
#assume all rows are the same length
looked_at = set()
islands_scouted = 0

for i in range(rows):
    for j in range(cols):
        if board[i][j] == 1 and (i, j) not in looked_at:
            scout_island(i, j)
            islands_scouted += 1

print(f'we found {islands_scouted} islands')