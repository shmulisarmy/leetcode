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

    def check_same_tree(self, other_tree):
        if self.value != other_tree.value:
            return False
        
        if not other_tree.right:
            if self.right:
                return False
            
        if not other_tree.left:
            if self.left:
                return False
        
        if not self.right:
            if other_tree.right:
                return False
            
        elif not self.right.check_same_tree(other_tree.right):
            return False
            
        if not self.left:
            if other_tree.left:
                return False
        elif not self.left.check_same_tree(other_tree.left):
            return False
            
        return True
        
        
        


main_tree = tree(5)
for i in [1, 4, 7, 2, 6, 3, 1, 3, 3, 3]: main_tree.insert(i)

second_tree = tree(5)
for i in [1, 4, 7, 2, 6, 3, 1, 3, 3, 3]: second_tree.insert(i)

print(main_tree.check_same_tree(second_tree))