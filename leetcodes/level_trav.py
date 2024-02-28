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

    def level_trav(self):
        stuff = [self.value]
        if self.left:
            stuff.append(self.left.level_trav())
        if self.right:
            stuff.append(self.right.level_trav())

        return stuff
            
main_tree = tree(5)
for i in [1, 4, 7, 3, 2]: main_tree.insert(i)

print(main_tree.level_trav())