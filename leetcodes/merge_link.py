class link:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        if self.next: self.next.insert(value)
        else: self.next = link(value)

    def merge(self, other):
        if not self.next: 
            return
        if other.value < self.next.value:
            temp = other.next
            other.next = self.next
            self.next = other
            self.next.merge(temp)
        else:
            self.next.merge(other)

    def trav(self):
        print(self.value)
        if self.next: self.next.trav()


            

link1 = link(1)
for i in [2, 3, 4, 6]: link1.insert(i)

link2 = link(2)
for i in [3, 4, 6, 8]: link2.insert(i)

link1.merge(link2)
link1.trav()