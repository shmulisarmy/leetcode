class link_list:
    def __init__(self, val):
        self.head = val
        self.next = None
    def insert(self, val):
        if self.next:
            self.next.insert(val)
        else:
            self.next = link_list(val)

    def pull_last(self):
        if not self.next.next:
            temp = self.next
            self.next = None
            return temp
        return self.next.pull_last()
    
    def reorder(self):
        temp = self.next
        self.next = self.pull_last()
        self.next.next = temp

    def trav(self):
        print(self.head)
        if self.next:
            self.next.trav()
            

main = link_list(4)

for i in range(10):
    main.insert(i)
main.trav()
print('\n\n\n')
main.reorder()
main.trav()


