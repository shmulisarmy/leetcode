class bst:
    def __init__(self, num) -> None:
        self.root = num
        self.right, self.left = None, None
    def insert(self, num):
        if num >= self.root:
            if self.right:
                self.right.insert(num)
            else:
                self.right = bst(num)
        
        if num < self.root:
            if self.left:
                self.left.insert(num)
            else:
                self.left = bst(num)

    def val(self):
        if self.right:
            if self.right.root < self.root:
                return False
            
        if self.left:
            if self.left.root < self.root:
                return False
            
        self.right.val()
        self.left.val()

    def depth(self):
        # max_depth = 0
        # if self.right:
        #     max_depth = max(max_depth, self.right.depth())
        # if self.left:
        #     max_depth = max(max_depth, self.left.depth())


        # return max_depth
        if self.right:
            right = self.right.depth()
        else:
            right = 0
        if self.left:
            left = self.left.depth()
        else:
            left = 0
        return max(right, left) + 1


main = bst(4)
for i in [1, 5, 0]:
    main.insert(i)

print(main.right.depth(), main.left.depth())