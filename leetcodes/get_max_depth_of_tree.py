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