def look_for_letter(row, col, letter):
    for i in range(row-1, row+1):
        for j in range(col-1, col+1):
            if in_bounds(i, j, board):
                if board[row][col] == letter:
                    return (row, col)
    return False



def in_board(board, word):
    looked_at = set()
    upto = 0
    for line, i in enumerate(board):
        for char, j in enumerate(line):
            if char == word[upto]:
                looked_at.add((i, j))


in_bounds = lambda row, col, board: (-1 < row < len(board)) and (-1 < col < len(board[0]))


board = [['a', 'l', 'p', 'r',
          'a', 'g', 'p', 'r',
          'a', 'o', 'p', 'p']]

