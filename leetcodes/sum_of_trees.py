class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left.insert = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right.insert = TreeNode(value)
            else:
                self.right.insert(value)

    def place(self, *values):
        for value in values:
            self.insert(value)

    def sum_(self):
        if self.left:
            left = self.left.sum_()
        else: 
            left = 0
        if self.right:
            right = self.right.sum_()
        else: 
            right = 0
        return [left[0]+right[0], 0]



main = TreeNode(4)
main.place(2, 4, 6, 2, 8, 1, 2)
        