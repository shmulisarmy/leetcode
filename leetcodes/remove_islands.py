def spread(row, col):
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i, j) in seen: continue
            if (-1 < i < len(board)) and (-1 < j < len(board[0]) and board[i][j] == 1):
                new_board[i][j] = 1
                seen.append((i, j))
                spread(i, j)


def find_connected_islands():
    for i in range(len(board)):
        for j in range(-1, 1):
            if board[i][j] == 1:
                if (i, j) in seen: continue
                new_board[i][j] = 1
                seen.append((i, j))
                spread(i, j)

    for i in range(len(board[0])):
        for j in range(-1, 1):
            if (j, i) in seen: continue
            if board[j][i] == 1:
                new_board[j][i] = 1
                seen.append((j, i))
                spread(j, i)






board = [[0, 0, 0, 1, 1, 0, 1],
         [0, 1, 0, 0, 0, 0, 1],
         [0, 1, 0, 1, 1, 0, 1],
         [1, 1, 0, 1, 1, 0, 1],
         [0, 1, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 1, 0, 1]]


new_board = [[0 for i in row] for row in board]
seen = []


find_connected_islands()

print(*new_board, sep = '\n')