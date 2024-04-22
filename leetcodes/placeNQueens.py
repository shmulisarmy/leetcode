from time import sleep

queensInCol = set()
queensIndiag = set()
queensInAntiDiag = set()


def placeQueens(board, row=0):
    print(*board, sep='\n')
    sleep(0.1)
    print()
    if row == size:
        return True
    for col in range(size):
        if board[row][col] == 'Q':
            continue
        if col in queensInCol or row - col in queensIndiag or row + col in queensInAntiDiag:
            continue
        board[row][col] = 'Q'
        queensInCol.add(col)
        queensIndiag.add(row - col)
        queensInAntiDiag.add(row + col)
        if placeQueens(board, row + 1):
            return True
        board[row][col] = '.'
        queensInCol.remove(col)
        queensIndiag.remove(row - col)
        queensInAntiDiag.remove(row + col)
        
    return False





size = 8
board = [
    ['.' for _ in range(size)] for _ in range(size)
    
]
print(f"{placeQueens(board) = }")