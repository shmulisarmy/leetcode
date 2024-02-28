board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0],
    [0,1,1,0,1,0,1,0,0],
    [0,1,1,0,0,0,0,0,0],
    [0,1,0,0,1,1,1,0,0],
    [0,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def hunt(row, column):
    seen.add((row, column))
    for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (row+i[0], column+i[1]) in seen:
            continue
        if -1 < row+i[0] < board_len and -1 < column+i[1] < row_len:
            if not board[row+i[0]][column+i[1]]:
                continue
            hunt(row+i[0], column+i[1])


seen = set()
islands = 0
board_len = len(board)
row_len = len(board[0])


for i, row in enumerate(board):
    for j, col in enumerate(row):
        if not col:
            continue
        if (i, j) in seen:
            continue
        islands+=1
        hunt(i, j)


print(f"{islands = }")
