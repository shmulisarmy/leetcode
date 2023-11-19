n = 2
def place_queens(cols_placed_in, row_minus_col, row_plus_col, row, number_of_placed_queens):
    number = 0
    for col in range(n): 
        print(f'{cols_placed_in = }, {row_minus_col = }, {row_plus_col = }')
        print(f'{row = }')
        print(f'{col = }')
        if col in cols_placed_in or row - col in row_minus_col or row + col in row_plus_col:
            continue
        number_of_placed_queens += 1
        print(f"{number_of_placed_queens = }")
        cols_placed_in.append(col)
        row_minus_col.append(row - col)
        row_plus_col.append(row + col)

        if number_of_placed_queens == n:
            return 1
        if row < n-1:
            number += place_queens(cols_placed_in, row_minus_col, row_plus_col, row+1, number_of_placed_queens)
        
        cols_placed_in.pop()
        row_minus_col.pop()
        row_plus_col.pop()

    return number
        
print(place_queens([], [], [], 0, 0))