""""takes in any sudoku board and solves it if posible
dynamic proggramming, runs in 10 to the eighty first"""


def valid(row, col, num):
    for i in range(9):
        if board[i][col] == num or board[row][i] == num:
            return False
    row_rounded_down = row - row%3
    col_rounded_down = col - col%3

    for row in range(row_rounded_down, row_rounded_down + 3):
        for col in range(col_rounded_down, col_rounded_down + 3):
            if board[row][col] == num:
                return False
    return True

def solve():
    for row in range(9):
        for col in range(9):
            if not board[row][col]:
                for num in range(1, 10):
                    if valid(row, col, num):
                        board[row][col] = num
                        if solve():
                            return True
                        board[row][col] = 0
                return False    
    return True

board = [[0 for _ in range(9)]for _ in range(9)]
solve()
for row in board:
    print(*row, sep= ' ')