""""takes in any sudoku board and solves it if posible
dynamic proggramming, runs in 10 to the eighty first"""


import time

def print_board() -> None:
    print()
    for row in board:
        print(*row, sep= ' ')


def valid(row: int, col: int, num):
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
    #show the algorithm solve the board step by step
    time.sleep(.04)
    print_board()

    for row in range(9):
        for col in range(9):
            if board[row][col]:
                continue
            for num in range(1, 10):
                if not valid(row, col, num):
                    continue
                board[row][col] = num
                if solve():
                    return True
                board[row][col] = 0
            return False    
    return True

board = [[0 for _ in range(9)]for _ in range(9)]
solve()