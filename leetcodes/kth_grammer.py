# row = 5
# col = 7

# class zeros_ones:
#     def __init__(self, number, depth = row, col = col):
#         self.col = col
#         self.number = number
#         if depth > 1:
#             rows_left = depth - 1
#             size_of_final_row = 2**(rows_left)
#             if self.col > size_of_final_row//2:
#                 self.col -= size_of_final_row//2
#                 next1 = zeros_ones(1 - number, depth - 1, self.col)
#             else:
#                 next1 = zeros_ones(number, depth - 1, self.col)
#         else:
#             print(number)
  
# zeros_ones(0)


row = 2
col = 1

cur = 0
left, right = 1, 2**(row-1)
for i in range(row):
    middle = (left + right) //2
    if col <= middle:
        right = middle
    else:
        left = middle + 1
        cur = 1 - cur

print(cur)
    
    