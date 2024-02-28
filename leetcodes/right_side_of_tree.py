class bst:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = bst(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = bst(value)

    def trav(self):
        print(self.value)


        if self.right:
            rights_values = self.right.trav()
        if self.left:
            lefts_values = self.left.trav()




que = []
main = bst(5)
for i in [9,3,8,7,2,9]:
    main.insert(i)



main.trav()
