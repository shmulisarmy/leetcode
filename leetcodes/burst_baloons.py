# baloons = [3, 1, 5, 8, 4]
# baloons = [1, 5, 8]

# def pop_last(index):
#     first = get_most(baloons[:index:])
#     if len(baloons) <= index + 1:
#         last = (1, 0)
#     else:
#         last = get_most(baloons[index + 1::])

#     return first[1] + first[0] * baloons[index] * last[0] + last[1]

# def get_most(mini_set):
#     if len(mini_set) == 1:
#         return (mini_set[0], 0)
    
#     best = 0
#     for i in range(len(mini_set)):
#         cur = pop_last(i)
#         if cur > best:
#             best = cur
#             best_one_to_keep_for_last = mini_set[i]

#     return (best_one_to_keep_for_last, best)

class tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, num):
        if num >= self.value:
            if not self.right:
                self.right = tree(num)
            else:
                self.right.insert(num)
        if num < self.value:
            if not self.left:
                self.left = tree(num)
            else:
                self.left.insert(num)

    def get_max_depth(self):
        if not self.right: 
            right_depth = 0
        else:
            right_depth = self.right.get_max_depth()
        if not self.left: 
            left_depth = 0
        else:
            left_depth = self.left.get_max_depth()
        return max(right_depth, left_depth) + 1


main_tree = tree(5)
for i in [1, 4, 7, 2, 6, 3, 1, 3, 3, 3]: main_tree.insert(i)

print(main_tree.get_max_depth())


#       5 
#    1      7 
# |    4   6
#     2
#      3