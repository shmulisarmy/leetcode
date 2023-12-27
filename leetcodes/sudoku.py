import time, copy

def valid(row, col, num, board):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    newrow = (row//3)*3
    newcol = (col//3)*3

    for i in range(3):
        for j in range(3):
            if board[newrow + i][newcol + j] == num:
                return False
            
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if valid(row, col, num, board):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


board1 = [[0] * 9 for i in range(9)]

for row in board1:
    print(*row, sep = ' ')
t = time.time()
solve(board1)
print(time.time() - t)

for row in board1:
    print(*row, sep = ' ')

