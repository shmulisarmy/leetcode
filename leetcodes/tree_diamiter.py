import sys 

class bst:
    m = 0
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.root:
            if not self.right:
                self.right = bst(value)
            else:
                self.right.insert(value)

        if value < self.root:
            if not self.left:
                self.left = bst(value)
            else:
                self.left.insert(value)

    def trav(self):
        if self.left:
            self.left.trav()

        print(self.root)

        if self.right:
            self.right.trav()

    """main function is that it updates bst.m but can only do so finding the max distance of indidual tree (dp type problem)"""
    def find_max_dist(self):
        if self.right:
            right_val = self.right.find_max_dist()
        else:
            right_val = 0

        if self.left:
            left_val = self.left.find_max_dist()
        else:
            left_val = 0

        bst.m = max(bst.m, right_val + left_val)

        return max(right_val, left_val) + 1

list = [11, 5, 4, 8, 3, 10, 20, 30, 2, 1, 0]
if len(sys.argv) > 2:
    list = [i for i in sys.argv[1::]]

main_tree = bst(list[0])
for i in list[1::]: main_tree.insert(i)
main_tree.find_max_dist()
print(bst.m)